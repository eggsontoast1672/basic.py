import dataclasses
import enum
from enum import Enum
from typing import Optional


class TokenKind(Enum):
    INTEGER = enum.auto()
    MINUS = enum.auto()
    PLUS = enum.auto()


@dataclasses.dataclass
class Token:
    kind: TokenKind
    text: Optional[str]
    start: int

    def __repr__(self) -> str:
        if self.text is None:
            return self.kind.name
        return f"{self.kind.name}({self.text})"


class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.index = 0
        self.current = None
        if self.index < len(self.text):
            self.current = self.text[self.index]

    def peek(self) -> Optional[str]:
        next_index = self.index + 1
        if next_index < len(self.text):
            return self.text[next_index]
        return None

    def advance(self) -> None:
        self.index += 1
        if self.index < len(self.text):
            self.current = self.text[self.index]
        else:
            self.current = None

    def integer(self) -> str:
        next = self.current
        digits: list[str] = []
        while next is not None and next.isdigit():
            digits.append(next)
            next = self.peek()
            if next is not None and next.isdigit():
                self.advance()
        return "".join(digits)


def lex(text: str) -> list[Token]:
    lexer = Lexer(text)
    tokens: list[Token] = []
    while lexer.current is not None:
        if lexer.current.isdigit():
            tokens.append(Token(TokenKind.INTEGER, lexer.integer(), lexer.index + 1))
        elif lexer.current == "-":
            tokens.append(Token(TokenKind.MINUS, None, lexer.index + 1))
        elif lexer.current == "+":
            tokens.append(Token(TokenKind.PLUS, None, lexer.index + 1))
        elif lexer.current.isspace():
            pass
        else:
            raise SyntaxError(f"stray '{lexer.current}' in program", (None, None, lexer.index + 1, None))
        lexer.advance()
    return tokens
