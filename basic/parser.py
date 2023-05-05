from typing import Optional

from lexer import Token, TokenKind


class NumberNode:
    def __init__(self, value: Token) -> None:
        self.value = value


class PlusNode:
    def __init__(self, left: NumberNode, right: NumberNode) -> None:
        self.left = left
        self.right = right


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

    def expression(self) -> PlusNode:
        if self.current.kind == TokenKind.NUMBER:
            left = NumberNode(self.current)
        self.advance()


def parse(tokens: list[Token]) -> Optional[PlusNode]:
    if len(tokens) == 0:
        return
    return Parser(tokens).expression()
