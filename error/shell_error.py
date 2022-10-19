class CommandNotFound(IndexError):
    def __init__(self, command_name, *args: object) -> None:
        super().__init__(f'{command_name}: not found', *args)