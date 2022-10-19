import re
import time
from command.model import CommandSet

class Sleep(CommandSet):
    _name = 'sleep'

    def command(self, *time_num):
        for time_arg in time_num:
            time_factor = 0
            time_number, suffix = re.match(
                r'(?P<time>\d+)(?P<suffix>(s|h|m)?)', str(time_arg)).group('time', 'suffix')
            
            if suffix == 'h':
                time_factor = 3600
            elif suffix == 'm':
                time_factor = 60
            elif suffix == 's':
                time_factor = 1
            
            # FIXME: be a bit strict about suffix
            # The current behavior is set all invalid suffix to second(s)
            elif suffix is None or suffix == '':
                time_factor = 1
            else:
                print(f'sleep: invalid interval time {time_arg}')
            time.sleep(float(time_number) * time_factor)