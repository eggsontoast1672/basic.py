import dataclasses
from lexer import Token, TokenKind


@dataclasses.dataclass
class NumberNode:
    token: Token

    def __repr__(self) -> str:
        return f"Number({self.token.text})"


@dataclasses.dataclass
class BinaryOperationNode:
    left: NumberNode
    operator: Token
    right: NumberNode

    def __repr__(self) -> str:
        return f"{self.operator}({self.left}, {self.right})"


class ParsingError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.index = 0
        self.current  = self.tokens[self.index]
        if len(self.tokens) == 0:
            self.current = None

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.tokens):
            self.current = self.tokens[self.index]
            return
        self.current = None

    def expr(self) -> BinaryOperationNode:
        if self.current is None:
            raise ParsingError("expected number, found nothing")
        if self.current.kind != TokenKind.NUMBER:
            raise ParsingError(f"expected number, found {self.current.kind}")
        left = NumberNode(self.current)
        self.advance()

        if self.current is None:
            raise ParsingError("expected plus operator, got nothing")
        if self.current.kind != TokenKind.PLUS:
            raise ParsingError(f"expected plus operator, got {self.current.kind}")
        operator = self.current
        self.advance()

        if self.current is None:
            raise ParsingError("expected number, found nothing")
        if self.current.kind != TokenKind.NUMBER:
            raise ParsingError(f"expected number, found {self.current.kind}")
        right = NumberNode(self.current)
        self.advance()

        return BinaryOperationNode(left, operator, right)

    def ast(self) -> BinaryOperationNode:
        return self.expr()
