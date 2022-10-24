import pathlib
from command.model import CommandSet


class RemoveFile(CommandSet):
    _name = 'rm'
    _aliases = ['del']

    def command(self, *args, **kwargs):
        if (len(args) > 0):
            file_path = pathlib.Path(args[0])
            if file_path.exists():
                file_path.unlink()
