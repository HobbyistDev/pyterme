import sys

def to_stdout(input_, end='\n', stdout_target=sys.stdout):
    if input:
        print(str(input_), end=end, file=stdout_target, flush=True)
    stdout_target.close()

def to_stderr(input_, end='\n',stderr_target=sys.stderr):
    if input:
        print(str(input_), end=end, file=stderr_target)
    stderr_target.close()