import re
import shlex

from .token import (
    Float,
    Integer,
    PipeToken,
    String,
    Token,
)


class ShellLexerBase:
    def __init__(self, text):
        self.text: str = text
        self.raw_token = []
        self.token_list = []

    def lex(self) -> list:
        self.set_token_value_list()
        self.tokenizer()
        return self.token_list

    def set_token_value_list(self):
        pass

    def tokenizer(self):
        self.token_list = []
        for index, token in enumerate(self.raw_token):
            token_type = 'undefined'

            # aritmethic
            if token == '+':
                token_type = 'Aritmethic'

            elif token == '-':
                token_type = 'Aritmethic'

            elif token == '/':
                token_type = 'Arithmetic'

            # Pipe symbol
            elif token == '>':
                token_type = PipeToken

            elif token == '>>':
                token_type = PipeToken

            elif token == '<':
                token_type = PipeToken

            elif token == '|':
                token_type = PipeToken

            # data type
            elif re.match(r'(\d+)', token):
                token_type = Integer

            elif re.match(r'(\d+\.\d+)', token):
                token_type = Float

            elif re.match(r'\w+', token):
                token_type = String

            if token_type != 'undefined':
                self.token_list.append(Token(token, token_type, index))


class RegexLexer(ShellLexerBase):
    def set_token_value_list(self) -> list[str]:
        pipe_pattern = r'2>|1>|>>|\|'
        number_pattern = r'd+'
        float_pattern = r'\d+\.\d+'
        string_pattern = r'w+'

        regex_pattern = rf'([{float_pattern}{number_pattern}|{pipe_pattern}|{string_pattern}])'
        self.raw_token: list[str] = (
            list(token.strip() for token in re.split(regex_pattern, self.text)
                 if token is not None))


class ShlexLexer(ShellLexerBase):
    def set_token_value_list(self) -> list:
        self.raw_token = list(shlex.shlex(self.text, punctuation_chars=True))
