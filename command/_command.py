from cat.cat import ConcatenateCommand

COMMAND_LIST = [
    class_ for name, class_ in globals().items()
    if name.endswith("Command")
]