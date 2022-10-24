import shutil
from command.model import CommandSet


class Which(CommandSet):
    _name = 'which'
    _aliases = ['where']

    def command(self, file_path=None, *args, **kwargs) -> str:
        if file_path is not None:
            if shutil.which(file_path) is not None:
                return shutil.which(file_path)
