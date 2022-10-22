import io
import pathlib
import sys

from util.logger import shell_logger

def to_stdout(input_, end='\n', stdout_target=sys.stdout):
    if stdout_target != sys.stdout:
        if isinstance(input_, (io.StringIO, io.FileIO, io.TextIOWrapper)):
            print(input_.read(), end=end, file=stdout_target, flush=True)
            input_.close()

        else:
            print(str(input_), end=end, file=stdout_target, flush=True)

        stdout_target.close()
        shell_logger.debug(f"pipe: to_stdout: {stdout_target.name} closed")

    elif isinstance(stdout_target, str) and pathlib.Path(stdout_target).exists():
        with pathlib.Path(stdout_target).open('w') as file:
            print(str(input_), end=end, file=file, flush=True)
    
    else:
        if input_:
            print(str(input_), end=end)

def to_stderr(input_, end='\n',stderr_target=sys.stderr):
    if stderr_target != sys.stderr:
        if input_:
            print(str(input_), end=end, file=stderr_target)
        stderr_target.close()
        shell_logger.debug(f"pipe: to_stderr: {stderr_target.name} closed")

    elif isinstance(stderr_target, str):
        with pathlib.Path(stderr_target) as file:
            print(str(input_), end=end, file=file, flush=True)

    else:
        if input_:
            print(str(input_), end=end)