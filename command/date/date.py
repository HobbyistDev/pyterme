import datetime

from command.model import CommandSet


class Date(CommandSet):
    _name = 'date'

    def command(self, *args, **kwargs):
        time_now = datetime.datetime.now()
        return time_now.strftime("%a %b %d %X %Z %Y")
