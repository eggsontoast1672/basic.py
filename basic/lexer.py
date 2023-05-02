import dataclasses
import enum
from enum import Enum


class TokenKind(Enum):
    NUMBER = enum.auto()
    PLUS = enum.auto()


@dataclasses.dataclass
class Token:
    kind: TokenKind
    text: str

    def __repr__(self) -> str:
        return f"{self.kind}({self.text})"


class LexingError(Exception):
    def __init__(self, message: str = "unrecognized token") -> None:
        super().__init__(message)


class Lexer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.index = 0
        self.current: str | None = self.code[self.index]

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.code):
            self.current = self.code[self.index]
            return
        self.current = None

    def number(self) -> Token:
        digits: list[str] = []
        while self.current is not None and self.current.isdigit():
            digits.append(self.current)
            self.advance()
        return Token(TokenKind.NUMBER, "".join(digits))

    def plus(self) -> Token:
        self.advance()
        return Token(TokenKind.PLUS, "+")

    def tokens(self) -> list[Token]:
        tokens: list[Token] = []
        while self.current is not None:
            if self.current.isdigit():
                tokens.append(self.number())
            elif self.current == "+":
                tokens.append(self.plus())
            elif self.current.isspace():
                self.advance()
            else:
                raise LexingError(f"unrecognized token {self.current}")
        return tokens
