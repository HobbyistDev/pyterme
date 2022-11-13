import pathlib

from util.color import colored_text


class ShellPipe:
    pass


class ShellStatusCode:
    pass


class ShellAppearance:
    def __init__(self, name, prompt_symbol, prompt_text):
        self.name = name
        self.prompt_symbol = prompt_symbol
        self.prompt_text = prompt_text


class ShellTheme:
    pass


class ShellParser:
    def __init__(self, text: str, parser_engine='default'):
        self.unparsed_text = text
        self.engine = parser_engine

    def _decide_engine(self, engine):
        if self.engine == 'default':
            pass

    def parse(self, log_level='warning'):
        pass


class ShellWarning:
    def __init__(self, msg: str):
        self.msg: str = msg

    def __str__(self) -> str:
        return f"{colored_text('WARNING', 'yellow') }: {self.msg}"


class ShellObject:
    def __init__(self, home_path=pathlib.Path().home()):
        self.home_path = home_path


class ShellEnvironment:
    def __init__(self, name, **kwargs):
        self.name: str = name
        self.kwargs = kwargs


class ShellCommandRunner:
    pass


class ShellCommandList:
    pass


class ShellLogger:
    pass
