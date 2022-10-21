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
from command.rm.rm import RemoveFile
from command.sleep.sleep import Sleep
from command.touch.touch import Touch
from command.uname.uname import UNIXName
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
    RemoveFile,
    SHA1Sum,
    SHA256Sum,
    Sleep,
    Touch,
    UNIXName,
    Which
]