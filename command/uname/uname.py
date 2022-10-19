import platform
from command.model import CommandSet

class UNIXName(CommandSet):
    _name = 'uname'

    def command(self, *args, **kwargs):
        uname_info = platform.uname()
        if not args:
            return platform.system()

        if '-a' in args:
            for info_ in uname_info:
                print(info_, end=' ')
            print('\n', end='')