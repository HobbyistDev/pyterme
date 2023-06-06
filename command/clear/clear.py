import os
from command.model import CommandSet


class Clear(CommandSet):
    """Clear all command that currently appear"""

    _name = 'clear'
    _aliases = ['cls']

    def command(self) -> None:
        os.system('cls||clear')

    def help(self):
        return """
        clear or cls is a command used for clear all previous output
        """
