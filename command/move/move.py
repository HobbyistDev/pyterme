import pathlib
import shutil
from command.model import CommandSet


class Move(CommandSet):
    _name = 'mv'
    _aliases = ['move']

    def command(self, src_path, dest_path, *args):
        src_path = pathlib.Path(src_path)
        dest_path = pathlib.Path(dest_path)

        if src_path.is_file() and dest_path.is_dir():
            shutil.move(src_path, dest_path)
