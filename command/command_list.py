from command.cat.cat import Concatenate
from command.cd.cd import ChangeDirectory
from command.clear.clear import Clear
from command.echo.echo import Echo
from command.hashsum.hashsum import (
    Base64,
    SHA1Sum, 
    SHA256Sum
)
from command.ls.ls import ListFile
from command.move.move import Move
from command.pwd.pwd import PrintWorkingDirectory
from command.sleep.sleep import Sleep
from command.which.which import Which

COMMAND_LIST = [
    Base64,
    ChangeDirectory,
    Clear,
    Concatenate,
    Echo,
    ListFile,
    Move,
    PrintWorkingDirectory,
    SHA1Sum,
    SHA256Sum,
    Sleep,
    Which
]