import pathlib
from command.model import CommandSet


class MakeDirectory(CommandSet):
    _name = 'mkdir'

    def command(self, *args, **kwargs):
        if (len(args) > 0):
            for arg in args:
                pathlib.Path.mkdir(arg, parents=True)
