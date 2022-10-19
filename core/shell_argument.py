import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--set-env', default='default', metavar='ENV',
    help=(
        '''set environment type in shell. This argument accept three option: \n
        Windows, linux, and default (default=\'default\')'''))
parser.add_argument(
    '--set-prompt-text-style', default='unix', metavar='prompt_style',
    help='''This command used to change the prompt to be looks like POSIX or Windows Prompt'''
)
args = parser.parse_args()
