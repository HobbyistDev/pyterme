import sys
from util.logger import shell_logger

def to_stdout(input_, end='\n', stdout_target=sys.stdout):
    if stdout_target != sys.stdout:
        if input_:
            print(str(input_), end=end, file=stdout_target, flush=True)
        stdout_target.close()
        shell_logger.debug(f"pipe: to_stdout: {stdout_target.name} closed")
    else:
        if input_:
            print(str(input_), end=end)

def to_stderr(input_, end='\n',stderr_target=sys.stderr):
    if stderr_target != sys.stderr:
        if input_:
            print(str(input_), end=end, file=stderr_target)
        stderr_target.close()
        shell_logger.debug(f"pipe: to_stderr: {stderr_target.name} closed")
    else:
        if input_:
            print(str(input_), end=end)