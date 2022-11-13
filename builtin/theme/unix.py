import getpass
import pathlib
import platform

from core.shell_api import ShellAppearance
from util.color import colored_text

current_dir = pathlib.Path().cwd()
prompt_prefix = colored_text(f"{getpass.getuser().lower()}@{platform.node()}", 'green')

try:
    UNIX_Prompt = ShellAppearance(
        'unix', '$',
        f"{prompt_prefix}:{colored_text(pathlib.Path().relative_to(current_dir).as_posix, 'blue', 'bold')}"
        )

except ValueError:
    UNIX_Prompt = ShellAppearance(
        'unix', '$',
        f'{prompt_prefix}:{colored_text(current_dir.as_posix(), "blue")}'
    )
