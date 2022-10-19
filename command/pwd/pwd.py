import pathlib
from command.model import CommandSet

class PrintWorkingDirectory(CommandSet):
    _name = 'pwd'

    def command(self, arg=None)-> pathlib.Path:
        if arg is None:
            return pathlib.Path.cwd()
        elif arg == '-L':
            pass
        elif arg == '-P':
            pass 