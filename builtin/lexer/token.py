import dataclasses
from typing import Any

TOKEN_LIST = ('+', '-', '/', '//')


@dataclasses.dataclass
class Token:
    value: Any
    type: object
    index: int


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
