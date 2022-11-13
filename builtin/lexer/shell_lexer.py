import re

from .token import (
    Float,
    Integer,
    PipeToken,
    String,
    Token,
)


class ShellLexer:
    def __init__(self, text):
        self.text: str = text

    def _set_to_tokens(self) -> list[str]:
        pipe_pattern = r'2>|1>|>>|\|'
        number_pattern = r'd+'
        string_pattern = r'w+'

        regex_pattern = rf'([{number_pattern}|{pipe_pattern}|{string_pattern}])'
        self.raw_token_list: list[str] = list(
                                    token.strip()
                                    for token in re.split(regex_pattern, self.text) if token is not None)
        # print(self.raw_token_list)
        self._token_type_matcher()
        return self.token_list

    def _token_type_matcher(self):
        self.token_list: list[Token] = []
        for token_index, token in enumerate(self.raw_token_list):
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
            elif re.match(r'\w+', token):
                token_type = String

            elif re.match(r'\d', token):
                token_type = Integer

            elif re.match(r'\d+\.\d+', token):
                token_type = Float

            if token_type != 'undefined':
                self.token_list.append(Token(token, token_type, token_index))

    def lex(self, log_level='warning'):
        pass
