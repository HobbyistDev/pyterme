import dataclasses
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time

from .logger import command_logger


class CommandSet:
    _name = None
    _aliases = []
    env_type = 'default'
    command_privilege = ['user']
 
    def __init__(self) -> None:
        pass 

    def create_name_alias(self, *aliases):
        for alias in aliases:
            self._aliases.extend(alias)

    def command(self, *args, **kwargs):
        '''Overide this class if the command is not platform specific'''
        command_logger.error("Not Implemented")

    def run_command(self, *args, **kwargs):
        if isinstance(self, list):
            raise TypeError(f'Wrong self type: {type(self)}')
        
        if self.env_type == 'linux':
            self.linux_specific_command(*args, **kwargs)
        elif self.env_type == 'windows':
            self.windows_specific_command(*args, **kwargs)
        elif self.env_type == 'default':
            self.command(*args, **kwargs)
        
        
    def linux_specific_command(self, *args, **kwargs):
        '''Overide this class if the command is specific to Linux'''
        command_logger.error("Not Implemented")

    def windows_specific_command(self, *args, **kwargs):
        '''Overide this class if the command is specific to Windows'''
        command_logger.error("Not Implemented")
    
    def get_name(self):
        return (self._name, self._aliases)

class Bash(CommandSet):
    _name = 'bash'

    def linux_specific_command(self, *args, **kwargs):
        program_args = ['bash'] + list(args)
        subprocess.run(program_args)

class Move(CommandSet):
    _name = 'mv'
    _aliases = ['move']

    def command(self, src_path, dest_path, *args):
        src_path = pathlib.Path(src_path)
        dest_path = pathlib.Path(dest_path)

        if src_path.is_file() and dest_path.is_dir():
            shutil.move(src_path, dest_path)

class Concat(CommandSet):
    _name = 'cat'

class Grep(CommandSet):
    _name = 'grep'

class Sleep(CommandSet):
    _name = 'sleep'

    def command(self, *time_num):
        time_num = time_num[0]
        time_number, suffix = re.match(
            r'(?P<time>\d+)(?P<suffix>(s|h|m)?)?', str(time_num)).group('time', 'suffix')
        if suffix == 'h':
            time_to_sleep = float(time_number) * 3600
        elif suffix == 'm':
            time_to_sleep = float(time_number) * 60
        elif suffix == 's' or suffix == None or suffix == '':
            time_to_sleep = float(time_number)
        else:
            raise ValueError(
                f'You Type invalid suffix: {suffix}.only h or m or s is allowed as suffix')
        time.sleep(time_to_sleep)

class ListFile(CommandSet):
    _name = 'ls'
    _aliases = ['dir']

class RemoveFile(CommandSet):
    _name = 'rm'
    _aliases = ['del']

class Echo(CommandSet):
    _name = 'echo'

    def command(self, *args, **kwargs):
        if len(args) == 0:
            pass
        elif len(args) == 1:
            print(args[0])
        else:
            for arg in args:
                print(arg, end=' ')
            print("\n", end='')


class PrintWorkingDirectory(CommandSet):
    _name = 'pwd'

    def command(self, arg=None):
        if arg is None:
            print(pathlib.Path.cwd())
        elif arg == '-L':
            pass
        elif arg == '-P':
            pass 

class ChangeDirectory(CommandSet):
    _name = 'cd'

    def command(self, *args, **kwargs):
        pass 

class MakeDirectory(CommandSet):
    _name = 'mkdir'

    def command(self, *args, **kwargs):
        pass 

class SuperUserDo(CommandSet):
    _name = 'sudo'
    _aliases = ['su']
    command_privilege = ['root']

    def command(self, *args, **kwargs):
        pass 

class Clear(CommandSet):
    _name = 'clear'
    _aliases = ['cls']

    def command(self):
        os.system('cls||clear')


class WhoAmI(CommandSet):
    _name = 'whoami'

class Exit(CommandSet):
    _name = 'exit'
    _aliases = ['quit', 'q', 'exit()']

    def command(self, *args, **kwargs):
        return sys.exit()


class Which(CommandSet):
    _name = 'which'
    _aliases = ['where']

    def command(self, file_path=None, *args, **kwargs):
        if file_path is not None:
            if shutil.which(file_path) is not None:
                print(shutil.which(file_path))

BASIC_UTIL_LIST = [
    Bash,
    Clear,
    Echo,
    Exit,
    Move,
    PrintWorkingDirectory,
    Sleep,
    Which,
]

def add_to_command_list(command_class):
    BASIC_UTIL_LIST.append(command_class)