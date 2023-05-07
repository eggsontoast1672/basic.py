import dataclasses
import textwrap
from typing import Union

from lexer import Token, TokenKind


@dataclasses.dataclass
class NumberNode:
    value: Token

    def __repr__(self) -> str:
        return repr(self.value)


@dataclasses.dataclass
class BinaryOperationNode:
    left: Union[NumberNode, "BinaryOperationNode"]
    right: NumberNode
    operator: Token

    def __repr__(self) -> str:
        return textwrap.dedent(f"""\
            BINARY_OPERATION(
                {self.left},
                {self.operator},
                {self.right}
            )\
        """)


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.index = 0
        self.current = None
        if self.index < len(self.tokens):
            self.current = self.tokens[self.index]

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.tokens):
            self.current = self.tokens[self.index]
        else:
            self.current = None

    def number(self) -> NumberNode:
        if self.current is None:
            raise SyntaxError(f"reached <EOF> while searching for {TokenKind.INTEGER}")
        if self.current.kind != TokenKind.INTEGER:
            raise SyntaxError(f"encountered unexpected token <{self.current}>", (None, None, self.current.start, None))
        return NumberNode(self.current)


def parse(tokens: list[Token]) -> Union[NumberNode, BinaryOperationNode]:
    parser = Parser(tokens)

    left = parser.number()
    parser.advance()
    while parser.current is not None:
        if parser.current.kind not in (TokenKind.PLUS, TokenKind.MINUS):
            raise SyntaxError(f"encountered unexpected token <{parser.current}>", (None, None, parser.current.start, None))
        operator = parser.current
        parser.advance()
        right = parser.number()
        left = BinaryOperationNode(left, right, operator)
        parser.advance()

    return left
