TOKEN_LIST = ('+', '-', '/', '//')


class Token:
    def __init__(self, token_value, token_type, token_index):
        self.value = token_value
        self.type = token_type
        self.index: int = token_index

    def __repr__(self) -> str:
        return f'Token(value={self.value}, type={self.type}, index={self.index})'


class AritmethicOperator:
    pass


class String:
    pass


class Add(AritmethicOperator):
    pass


class Substract(AritmethicOperator):
    pass


class Division(AritmethicOperator):
    pass


class Multiply(AritmethicOperator):
    pass


class Modulus(AritmethicOperator):
    pass


class EOF:
    pass


class PipeToken:
    pass


class Integer:
    pass


class Float:
    pass


class UndefinedToken:
    pass
