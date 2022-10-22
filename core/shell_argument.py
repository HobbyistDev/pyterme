import argparse

parser = argparse.ArgumentParser(
    prog='pyterme', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '--log-level', default='warning', metavar='level', 
    help='Set log level to a levelname. This argument only take effect in stdout')

# shell customization
shell_customization_parser = parser.add_argument_group('Shell Customization Option')
shell_customization_parser.add_argument(
    '--set-env', default='default', metavar='ENV',
    help=(
        '''set environment type in shell. This argument accept three option: \n
        Windows, linux, and default'''))

shell_customization_parser.add_argument(
    '--set-prompt-text-style', default='unix', metavar='prompt_style',
    help='''This command used to change the prompt to be looks like POSIX or Windows Prompt'''
)

shell_customization_parser.add_argument(
    '--set-prompt-symbol', default=None, metavar='symbol',
    help='Set particular prompt symbol to terminal. This option didn\'t take effect when --set-prompt-text-style set to windows'
)

args = parser.parse_args()
