import pathlib
import re
import sys
import fileinput

from command.model import CommandSet
from util.color import colored_text


class Grep(CommandSet):
    _name ='grep'

    def command(self, pattern, *args, **kwargs):
        # only set file args if the string is a path not argument
        file_args = [arg for arg in args if pathlib.Path(arg).exists()]

        # if no args, read from stdin
        # TODO: give newline in the end of string matching if args > 1
        for line in fileinput.input(file_args):
            if re.match(rf'.*(\b{pattern}).*', line.rstrip()):
                matched_text = re.match(rf'.*(\b{pattern}).*', line.rstrip()).group(0)
                print(colored_text(matched_text, 'red', 'bold'))

        # if args specified, check from the args