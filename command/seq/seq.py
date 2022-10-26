from command.model import CommandSet


class Sequence(CommandSet):
    _name = 'seq'

    def command(self, *args, **kwargs):
        total_args = len(args)

        if total_args == 1:
            for number in range(1, int(args[0]) + 1, 1):
                print(number)

        elif total_args == 2:
            for number in range(int(args[0]), int(args[1]) + 1, 1):
                print(number)

        elif total_args == 3:
            for number in range(int(args[0]), int(args[2]) + 1, int(args[1])):
                print(number)
