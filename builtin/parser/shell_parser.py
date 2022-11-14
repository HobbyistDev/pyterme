from command.command_api import CommandRunner


class ShellParserBase:
    def __init__(self, token_list):
        self.token_list: list = token_list
        self.pos: int = -1
        self.current_token = None

    def get_next_token(self, token_number=1):
        print(self.current_token, self.pos)
        if self.pos == -1:
            self.current_token = self.token_list[0]
            self.pos = self.pos + 1

        elif self.pos + token_number < len(self.token_list):
            self.current_token = self.token_list[self.pos + token_number]
            self.pos = self.pos + token_number

        return None

    def parse_pipe(self):
        skip_number_of_token = 1

        pipe_target = self.token_list[self.pos + 1]
        command_process = CommandRunner()
        command_process.run_command(self.token_list[self.pos - 1])

        if self.current_token == '>':
            parse_stdout(command_process.stdout, pipe_target)
            skip_number_of_token = 2

        elif self.current_token == '>>':
            parse_stderr(command_process.stdout, pipe_target)
            skip_number_of_token = 2

        self.get_next_token(skip_number_of_token)

    def consume_token(self):
        # CAUTION: this code is not finished yet, it can lead to
        # infinite loop
        while (self.pos < len(self.token_list)):
            self.get_next_token()

            if self.current_token in ('>', '>>'):
                self.parse_pipe()
                break

    def reset_token_list(self):
        pass

    def parse(self):
        self.consume_token()


def parse_stdout(command_output, file_output):
    if command_output is not None and file_output is not None:
        with open(file_output, mode='wb') as file:
            file.write(command_output)


def parse_stderr(command_output, file_output):
    if command_output is not None and file_output is not None:
        with open(file_output, mode='wb') as file:
            file.write(command_output)
