from util.color import colored_text


class ShellError(Exception):
    def __init__(self, msg: str, error_code: int = 1):
        self.msg: str = msg
        self.error_code: int = error_code

    def __str__(self) -> str:
        return f"{colored_text('ERROR', 'red', 'bold') }: {self.msg} with exit code {self.error_code}"
