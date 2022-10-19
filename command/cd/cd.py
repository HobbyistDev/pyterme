import pathlib
import os
from command.model import CommandSet, command_logger

class ChangeDirectory(CommandSet):
    _name = 'cd'

    def __init__(self, env='default') -> None:
        super().__init__(env)
        self.supported_env = ['default', 'windows']

    def command(self, *args, **kwargs):
        '''This command will use unix like command'''
        if (len(args) == 0):
            # in *nix, cd point to home environment if args not supplied
            os.chdir(str(pathlib.Path.home()))
        elif (len(args) == 1):
            if (pathlib.Path(args[0]).exists()):
                os.chdir(args[0])
            else:
                command_logger.info(f"{args[0]}: no such file or directory")
                print(f"{args[0]}: no such file or directory")

    def windows_specific_command(self, *args, **kwargs) -> str:
        if (len(args) == 0) or list(args) == []:
            return pathlib.Path.cwd()
        else:
            command_logger.info(f"The system cannot find the path specified.")
            print(f"The system cannot find the path specified.")

    