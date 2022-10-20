import argparse
import functools
import getpass
import pathlib
import platform
import sys
import shutil
import shlex
import subprocess

from command.command_list import COMMAND_LIST
from core.shell_argument import args as shell_args
from core.shell_conf_parser import shell_set_configuration
from util.logger import logger, shell_logger
from util.color import colored_text
from util.pipe_util import to_stdout, to_stderr


# TODO: add shell redirection feature (stdout, stderr, etc)
class Shell:
    _privilege = 'user'

    def __init__(self, prompt='$', env='default', username=None, prompt_text_style='unix'):
        self.username = getpass.getuser() if username is None else str(username)
        self.home_dir = pathlib.Path().resolve()
        self.prompt_symbol = prompt
        self.prompt_text_style = prompt_text_style
        self.set_prompt(prompt, env, prompt_text_style=self.prompt_text_style)

        # default pipe
        self.stdout_target = sys.stdout
        self.stderr_target = sys.stderr

        self.is_running = True
        self.shell_start()
        self.main_loop()
        self.shell_stop()
    
    def set_prompt(self, prompt='$', env='default', color='auto', prompt_text_style='unix'):
        """
        This method set prompt text looks like.
        @param  prompt  Set prompt_symbol in terminal (default: $)
        @param  env     Set terminal_environment (default: 'default')
        @param  color   Decide if terminal is using color or not (default: 'auto')
        @param  prompt_text_style   Set prompt look to be POSIX-like or Windows-like(default: 'unix')
        """
        current_path = pathlib.Path.cwd()

        if color in ('auto', 'always'):
            if prompt_text_style == 'unix':
                prompt_text = colored_text(f"{self.username.lower()}@{platform.node()}", 'green')

                if current_path == self.home_dir:
                    self.prompt = f"{prompt_text}:{colored_text('~', 'blue')}{prompt}"
                else:
                    try:
                        self.prompt = f"{prompt_text}:{colored_text(f'~/{current_path.relative_to(self.home_dir).as_posix()}', 'blue')}{prompt}"
                    except ValueError:
                        self.prompt = f"{prompt_text}:{colored_text(current_path.as_posix(), 'blue')}{prompt}"

            if prompt_text_style == 'windows':
                self.prompt = f"{current_path}>"

        
        self.env_type = env

    def shell_start(self):
        """
        Override this method to give start text
        or another thing that you want to start before
        the mainloop run
        """
        print('Welcome to this terminal!')
        print('Current Setting: ')
        print(f'ENV: {self.env_type}', end=' | ') 
        print(f'Prompt_symbol: {self.prompt_symbol}', end=' | ')
        print(f'Prompt_style: {self.prompt_text_style}')

   

    def main_loop(self):
        # TODO: improve command matching, parsing
        while(self.is_running):

            basic_cmd_name = [cmd._name for cmd in COMMAND_LIST]
            #print(basic_cmd_list)

            user_input = input(f'{self.prompt} ')
            self.parse_command_string(user_input)

            self.set_prompt(self.prompt_symbol, self.env_type, prompt_text_style=self.prompt_text_style)

    def shell_stop(self):
        pass 

    def parse_command_string(self, user_input):
        program_input = []
        
        basic_cmd_list = [
            cmd(env=self.env_type).get_name() 
            for cmd in COMMAND_LIST
        ]

        user_cmd = list(shlex.shlex(user_input, punctuation_chars=True))  # TODO: handle quoted argument
        
        program_input.extend(user_cmd)

        IS_CMD_IN_BASIC_CMD_lIST = False

        # pipe handle
        if '>' in user_cmd and user_cmd.index('>') < len(user_cmd) and user_cmd.index('>') != 0 and user_cmd[user_cmd.index('>') - 1] != '2':
            self.stdout_target = user_cmd[user_cmd.index('>') + 1]
            shell_logger.debug(f"pipe: trying to open {self.stdout_target}")
            
            self.stdout_target = pathlib.Path(self.stdout_target).open('w')
            shell_logger.info(f'stdout_target: {self.stdout_target}')

        elif '|' in user_cmd and user_cmd.index('|') < len(user_cmd) and user_cmd.index('|') != 0:
            self.pipe_target = user_cmd[user_cmd.index('|') + 1]

        elif '2>' in user_cmd and user_cmd.index('2>') < len(user_cmd) and user_cmd.index('2>') != 0:
            self.stderr_target = user_cmd[user_cmd.index('2>') + 1]

        
        if user_input == '' or len(user_input[0]) == 0:
            pass 
        else:
            # TODO: reduce for-loop usage
            for cmd in basic_cmd_list:
                command_name, command_aliases = cmd
                    
                if user_cmd[0] == command_name or user_cmd[0] in command_aliases:
                    shell_logger.info(f"{user_cmd[0]} executed from basic_cmd_list: {command_name}")
                    cmd_index = basic_cmd_list.index(cmd)

                    command_to_run = COMMAND_LIST[cmd_index](env=self.env_type)
                    command_to_run.set_pipe(self.stdout_target)
                    command_to_run.run_command(*user_cmd[1:])
                    IS_CMD_IN_BASIC_CMD_lIST = True
                    break
                else:
                    continue

            if user_input == '' or len(user_input[0]) == 0:
                pass 

            elif IS_CMD_IN_BASIC_CMD_lIST:
                IS_CMD_IN_BASIC_CMD_lIST = False
            
            elif user_input in ('quit', 'exit', 'exit()', 'q'):
                self.is_running = False
            
            elif shutil.which(user_cmd[0]):
                shell_logger.info("Executed from shutil.which")

                # set pipe only if stdout_target and stderr_target is not the same as the default
                if self.stdout_target == sys.stdout and self.stderr_target == sys.stderr:
                    subprocess.run(user_input)
                else:
                    process = subprocess.run(user_input, capture_output=True)
                    if process.stdout:
                        to_stdout(process.stdout.decode(), stdout_target=self.stdout_target)
                    if process.stderr:
                        to_stderr(process.stderr.decode(), stderr_target=self.stderr_target)
                
            
            elif user_cmd[0] in ('sudo', 'su'):
                is_authenticated = self.authenticate_user()
                if is_authenticated:
                    self.elevate_privilege()

            else:
                shell_logger.info(f"{user_cmd[0]} not found")
                #print(f'{user_cmd[0]}: not found')
                to_stdout(f'{user_cmd[0]}: not found', stdout_target=self.stdout_target)

    def authenticate_user(self) -> bool:
        MAX_NUMBER_LOGIN_ATTEMPT = 3
        NUMBER_OF_LOGIN_ATTEMPT = 0

        while (NUMBER_OF_LOGIN_ATTEMPT < MAX_NUMBER_LOGIN_ATTEMPT):
            password = getpass.getpass(f'password for {getpass.getuser()}: ')
            if password == 'terminal':
                return True
            else:
                print('Sorry, try again')
                NUMBER_OF_LOGIN_ATTEMPT += 1
        print(f'sudo: {NUMBER_OF_LOGIN_ATTEMPT} incorrect password attempts')
        return False
    
    def elevate_privilege(self):
        self.make_shell('#', self.env_type, 'root')
    
    @classmethod
    def make_shell(cls, prompt='$', env='default', username=None):
        cls(prompt, env, username)


class UserShell(Shell):
    def su(self):
        # start admin shell
        SuperUserShell()

class SuperUserShell(Shell):
    prompt = '#'
    _privilege = 'root'

    def is_authenticated(self, password):
         # Only for testing !
        if password != 'root':
            return False
        else:
            print("authenticated")
            return True
    
    def set_prompt(self, prompt='#', env='default'):
        return super().set_prompt(prompt, env)

    def shell_start(self):
        i = 0
        max_number_of_attempt = 3
        self.is_running = False
        while (i < max_number_of_attempt):
            password = getpass.getpass()
            self.is_running = self.is_authenticated(password)
            if not self.is_running:
                i = i + 1
            else:
                break

def main():
    if len(sys.argv) > 1:
        terminal_prompt_symbol = shell_args.set_prompt_symbol
        terminal_env = shell_args.set_env
        terminal_prompt_text_style = shell_args.set_prompt_text_style

    elif shell_set_configuration():
        shell_conf = shell_set_configuration()
        terminal_prompt_symbol = shell_conf.get('prompt_symbol')
        terminal_env = shell_conf.get('environment')
        terminal_prompt_text_style = shell_conf.get('prompt_text_style')

    UserShell(
        prompt=terminal_prompt_symbol, env=terminal_env, prompt_text_style=terminal_prompt_text_style)

if __name__ == '__main__':
    main()