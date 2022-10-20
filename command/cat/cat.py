import pathlib
import sys
import fileinput
from command.model import CommandSet

from util.pipe_util import to_stdout, to_stderr
from util.logger import command_logger

class Concatenate(CommandSet):
    _name = 'cat'

    def command(self, *args, **kwargs):
        if len(args) == 1:
            if pathlib.Path(args[0]).exists():
                with open(pathlib.Path(args[0])) as file:
                    to_stdout(file.read(), stdout_target=self.stdout_target)
        if len(args) == 0:
            # if none of stdout redirection
            for line in fileinput.input():
                to_stdout(line.rstrip(), stdout_target=self.stdout_target)