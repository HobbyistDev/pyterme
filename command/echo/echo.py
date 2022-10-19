from command.model import CommandSet

class Echo(CommandSet):
    _name = 'echo'

    def command(self, *args, **kwargs):
        if len(args) == 0:
            pass
        elif len(args) == 1:
            return args[0]
        else:
            for arg in args:
                print(arg, end=' ')
            print("\n", end='')