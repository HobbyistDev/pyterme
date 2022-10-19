import pathlib
import os
from command.model import CommandSet
from util.color import print_colored

class ListFile(CommandSet):
    _name = 'ls'

    def command(self, *args, **kwargs):
        command_result = []
        if len(args) == 0:
            command_result = pathlib.Path('.').glob('*')
        elif len(args) == 1:
            if pathlib.Path(args[0]).exists():
                command_result = [file_path.name for file_path in pathlib.Path(args[0]).glob("*")]

        # TODO: check based on magic number not by ext 
        for path in command_result:
            if path.is_dir():
                print_colored(path, 'bright_blue')
            elif path.suffix in ('.exe', '.com', '.bat', '.vbs'):
                print_colored(path, 'bright_green')
            elif path.suffix in ('zip', '.7z'):
                print_colored(path, 'bright_red')
            elif path.is_file():
                print(path)
            