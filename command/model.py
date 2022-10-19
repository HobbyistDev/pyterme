from util.logger import command_logger

class CommandSet:
    _name = None
    _aliases = []
    env_type = 'default'
    command_privilege = ['user']
    supported_env = ['default']
 
    def __init__(self, env='default') -> None:
        self.env_type = env
        self.supported_env = ['default']
        self.__command_post_init()
    
    def __command_post_init(self):
        pass 

    def command(self, *args, **kwargs):
        '''
        Overide this class if the command is not platform specific.\n
        This method is required to defined in every command.\n\n
        '''
        command_logger.error("Not Implemented")
        raise NotImplementedError

    def run_command(self, *args, **kwargs):
        if isinstance(self, list):
            raise TypeError(f'Wrong self type: {type(self)}')
        
        command_result = None
        if self.env_type in self.supported_env:
            
            if self.env_type == 'linux':
                command_result = self.linux_specific_command(*args, **kwargs)
            elif self.env_type == 'windows':
                command_result = self.windows_specific_command(*args, **kwargs)
            elif self.env_type == 'default':
                command_result = self.command(*args, **kwargs)
        else:
            # set to default when supported env not found
            command_result = self.command(*args, **kwargs)
        
        if command_result:
            print(command_result)
        
        
    def linux_specific_command(self, *args, **kwargs):
        '''Overide this class if the command is specific to Linux'''
        command_logger.error("Not Implemented")

    def windows_specific_command(self, *args, **kwargs):
        '''Overide this class if the command is specific to Windows'''
        command_logger.error("Not Implemented")
    
    def help(self):
        pass

    def get_name(self):
        return (self._name, self._aliases)
    
    def change_env(self, env):
        self.env_type = env
    