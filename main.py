import argparse
import functools
import getpass
import pathlib
import platform
import sys
import shutil
import shlex
import subprocess

from command.command_list import COMMAND_LIST
from util.logger import logger, shell_logger
from util.color import print_colored


# TODO: add shell redirection feature (stdout, stderr, etc)
class Shell:
    _privilege = 'user'

    def __init__(self, prompt='$', env='default', username=None):
        self.username = getpass.getuser() if username is None else str(username)
        self.set_prompt(f'{self.username.lower()}{prompt}', env)

        self.is_running = True
        self.shell_start()
        self.main_loop()
        self.shell_stop()
    
    def set_prompt(self, prompt='$', env='default'):
        self.prompt = prompt
        self.env_type = env

    def shell_start(self):
        """
        Override this method to give start text
        or another thing that you want to start before
        the mainloop run
        """
        print('Welcome to this terminal!')
        print('Current Setting: ')
        print(f'ENV: {self.env_type}') 

   

    def main_loop(self):
        # TODO: improve command matching, parsing
        while(self.is_running):

            basic_cmd_name = [cmd._name for cmd in COMMAND_LIST]
            
            

            #print(basic_cmd_list)

            

            user_input = input(f'{self.prompt} ')
            self.parse_command_string(user_input)

    def shell_stop(self):
        pass 

    def to_stdout(self, input_):
        if input:
            #print(str(input_), end='', file=sys.stdout)
            print_colored(str(input_), end='', file=sys.stdout)
    
    def to_stderr(self, input_):
         if input:
            print(str(input_), end='', file=sys.stderr)
    
    def parse_command_string(self, user_input):
        program_input = []
        
        basic_cmd_list = [
            cmd(env=self.env_type).get_name() 
            for cmd in COMMAND_LIST
        ]

        user_cmd = list(shlex.shlex(user_input, punctuation_chars=True))  # TODO: handle quoted argument
        
        program_input.extend(user_cmd)

        IS_CMD_IN_BASIC_CMD_lIST = False
        
        if user_input == '' or len(user_input[0]) == 0:
            pass 
        else:
            # TODO: reduce for-loop usage
            for cmd in basic_cmd_list:
                command_name, command_aliases = cmd
                    
                if user_cmd[0] == command_name or user_cmd[0] in command_aliases:
                    shell_logger.info(f"{user_cmd[0]} executed from basic_cmd_list: {command_name}")
                    cmd_index = basic_cmd_list.index(cmd)
                    COMMAND_LIST[cmd_index](env=self.env_type).run_command(*user_cmd[1:])
                    IS_CMD_IN_BASIC_CMD_lIST = True
                    break
                else:
                    continue

            if user_input == '' or len(user_input[0]) == 0:
                pass 

            elif IS_CMD_IN_BASIC_CMD_lIST:
                IS_CMD_IN_BASIC_CMD_lIST = False
                    
            elif shutil.which(user_cmd[0]):
                shell_logger.info("Executed from shutil.which")
                subprocess.run(user_input)#, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            elif user_input in ('quit', 'exit', 'exit()', 'q'):
                self.is_running = False
            
            elif user_cmd[0] in ('sudo', 'su'):
                is_authenticated = self.authenticate_user()
                if is_authenticated:
                    self.elevate_privilege()

            else:
                shell_logger.info(f"{user_cmd[0]} not found")
                print(f'{user_cmd[0]}: not found')

    def authenticate_user(self) -> bool:
        MAX_NUMBER_LOGIN_ATTEMPT = 3
        NUMBER_OF_LOGIN_ATTEMPT = 0
        username = getpass.getuser()
        password = getpass.getpass()

        while (NUMBER_OF_LOGIN_ATTEMPT < MAX_NUMBER_LOGIN_ATTEMPT):
            if password == 'terminal':
                return True
            else:
                NUMBER_OF_LOGIN_ATTEMPT += 1
        return False
    
    def elevate_privilege(self):
        self.make_shell('#', self.env_type, 'root')
    
    @classmethod
    def make_shell(cls, prompt='$', env='default', username=None):
        cls(prompt, env, username)




class UserShell(Shell):
    def su(self):
        # start admin shell
        SuperUserShell()

class SuperUserShell(Shell):
    prompt = '#'
    _privilege = 'root'

    def is_authenticated(self, password):
         # Only for testing !
        if password != 'root':
            return False
        else:
            print("authenticated")
            return True
    
    def set_prompt(self, prompt='#', env='default'):
        return super().set_prompt(prompt, env)

    def shell_start(self):
        i = 0
        max_number_of_attempt = 3
        self.is_running = False
        while (i < max_number_of_attempt):
            password = getpass.getpass()
            self.is_running = self.is_authenticated(password)
            if not self.is_running:
                i = i + 1
            else:
                break
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--set-env', default='default', metavar='ENV',
        help=(
            '''set environment type in shell. This argument accept three option: \n
            Windows, linux, and default (default=\'default\')'''))
    args = parser.parse_args()

    UserShell(env=args.set_env)

if __name__ == '__main__':
    main()