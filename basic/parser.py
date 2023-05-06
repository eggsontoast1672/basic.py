import dataclasses
import textwrap
from typing import Optional

from lexer import Token, TokenKind


@dataclasses.dataclass
class NumberNode:
    value: Token

    def __repr__(self) -> str:
        return repr(self.value)


@dataclasses.dataclass
class PlusNode:
    left: NumberNode
    right: NumberNode

    def __repr__(self) -> str:
        return textwrap.dedent(f"""\
            PLUS(
                {self.left},
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

    def check_current_kind(self, expected: TokenKind) -> Token:
        if self.current is None:
            raise SyntaxError(f"expected <{expected.name}>, got <EOF>")
        if self.current.kind != expected:
            raise SyntaxError(f"expected <{expected.name}>, got <{self.current.kind.name}>", (None, None, self.current.start, None))
        return self.current

    def number(self) -> NumberNode:
        node = NumberNode(self.check_current_kind(TokenKind.INTEGER))
        self.advance()
        return node

    def expression(self) -> PlusNode:
        left = self.number()

        self.check_current_kind(TokenKind.PLUS)
        self.advance()

        right = self.number()

        return PlusNode(left, right)


def parse(tokens: list[Token]) -> Optional[PlusNode]:
    tokens.append(Token(TokenKind.EOF, None))
    return Parser(tokens).expression()
