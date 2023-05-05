import enum
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TokenKind(Enum):
    NUMBER = enum.auto()
    PLUS = enum.auto()


@dataclass
class Token:
    kind: TokenKind
    text: str

    def __repr__(self) -> str:
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

    def number(self) -> str:
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
            tokens.append(Token(TokenKind.NUMBER, lexer.number()))
        elif lexer.current == "+":
            tokens.append(Token(TokenKind.PLUS, lexer.current))
        elif lexer.current.isspace():
            pass
        else:
            raise SyntaxError("invalid syntax", ("stdin", 1, lexer.index + 1, text))
        lexer.advance()
    return tokens
