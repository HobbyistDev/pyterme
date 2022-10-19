import pathlib
from command.model import CommandSet

class Touch(CommandSet):
    _name = 'touch'

    def command(self, *args, **kwargs):
        if len(args) == 1:
            pathlib.Path(args[0]).touch()