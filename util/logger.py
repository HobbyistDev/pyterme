import logging
from core.shell_argument import args as shell_args


LOG_LEVEL: set = {'debug', 'info', 'warning', 'error', 'critical'}

# app logger
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

stream_handler = logging.StreamHandler()
stream_handler.setLevel("WARNING")

logger.addHandler(stream_handler)

# command logger
command_logger = logging.getLogger('command_logger')
command_logger.setLevel("DEBUG")

command_stream_handler = logging.StreamHandler()
command_stream_handler.setLevel("WARNING")

command_logger.addHandler(command_stream_handler)


# shell logger

shell_log_level_args = shell_args.log_level.upper() if shell_args.log_level in LOG_LEVEL else None

shell_logger = logging.getLogger(__name__)
shell_logger.setLevel("DEBUG")


shell_formatter = logging.Formatter("[shell] [%(levelname)s] %(message)s")

shell_stream_handler = logging.StreamHandler()
shell_stream_handler.setLevel(shell_log_level_args or "WARNING")
shell_stream_handler.setFormatter(shell_formatter)


shell_logger.addHandler(shell_stream_handler)
