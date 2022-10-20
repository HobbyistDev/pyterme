import platform
from command.model import CommandSet
from util.pipe_util import to_stdout

class UNIXName(CommandSet):
    _name = 'uname'

    def command(self, *args, **kwargs):
        uname_info = platform.uname()
        if not args:
            return platform.system()

        if '-a' in args:
            for info_ in uname_info:
                to_stdout(info_, end=' ', stdout_target=self.stdout_target)
            to_stdout('\n', end='', stdout_target=self.stdout_target)