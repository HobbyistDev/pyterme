import os
from command.model import CommandSet


class Clear(CommandSet):
    _name = 'clear'
    _aliases = ['cls']

    def command(self) -> None:
        os.system('cls||clear')

    def help(self):
        return """
        clear or cls is a command used for clear all previous output
        """
