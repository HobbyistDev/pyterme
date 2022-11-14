import shutil
import subprocess


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


class CommandRunner:
    def __init__(self):
        # program return
        self.stdout = None
        self.stderr = None
        self.stdin = None
        self.status_code = None

    def run_command(self, *command_args):
        if shutil.which(command_args[0]):
            # handling command in subprocess if avaiable in path
            process = subprocess.run(list(command_args), capture_output=True)
            self.stdout, self.stderr = process.stdout, process.stderr
            self.status_code = process.returncode
        return (self.stdout, self.stderr, self.status_code)
