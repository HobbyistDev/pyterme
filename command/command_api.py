class CommandBaseClass:
    _version = None

    def show_version(self):
        return self._version


class CommandArgumentParser:
    pass


class CommandFlag:
    def __init__(self, command_type, command_help):
        self.type = command_type  # can optional or positional
        self.help = command_help


class CommandStandardOutput:
    pass


class CommandStandardInput:
    pass


class CommandStandardError:
    pass
