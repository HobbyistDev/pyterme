import argparse
import json
import pathlib

from command.model import CommandSet
from util.color import colored_text


class ListFile(CommandSet):
    _name = 'ls'

    def command(self, *args, **kwargs):
        ls_conf = get_configuration()
        command_result = []
        if len(args) == 0:
            command_result = pathlib.Path('.').glob('*')
        elif len(args) == 1:
            if pathlib.Path(args[0]).exists():
                command_result = [file_path.name for file_path in pathlib.Path(args[0]).glob("*")]

        # TODO: check based on magic number not by ext
        color_conf = ls_conf.get('color', {})
        for path in command_result:
            # if path is directory
            if path.is_dir():
                # print_colored(path, 'bright_blue')
                print(colored_text(path, color_conf.get('directory') or 'blue', 'bold'))

            # if path is executables
            elif path.suffix in ('.exe', '.com', '.bat', '.vbs'):
                print(colored_text(path, color_conf.get('executables') or 'green', 'bold'))

            # if path is archive
            elif path.suffix in ('zip', '.7z'):
                print(colored_text(path, color_conf.get('archive') or 'red', 'bold'))

            # if path is regular file
            elif path.is_file():
                print(path)


def get_configuration():
    # TODO: use __file__ alternative as __file__ didn't always exist
    json_conf_file = {}
    with open(pathlib.Path(__file__).parent / "ls_conf.json") as conf_file:
        json_conf_file = json.load(conf_file)
    return json_conf_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l')
    args = parser.parse_known_args()

    command = ListFile()
    command.run_command()