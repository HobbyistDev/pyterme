import pathlib
import sys
from command.model import CommandSet

class Concatenate(CommandSet):
    _name = 'cat'

    def command(self, *args, **kwargs):
        if len(args) == 1:
            if pathlib.Path(args[0]).exists():
                with open(pathlib.Path(args[0])) as file:
                    print(file.read())