import enum
from dataclasses import dataclass
from enum import Enum


class TokenKind(Enum):
    NUMBER = enum.auto()
    PLUS = enum.auto()


@dataclass
class Token:
    kind: TokenKind
    text: str

    def __repr__(self) -> str:
        return f"{self.kind.name}({self.text})"


def lex(text: str) -> list[Token]:
    tokens: list[Token] = []
    for offset, character in enumerate(text, start=1):
        if character.isdigit():
            tokens.append(Token(TokenKind.NUMBER, character))
        elif character == "+":
            tokens.append(Token(TokenKind.PLUS, character))
        elif character.isspace():
            pass
        else:
            raise SyntaxError("invalid syntax", ("stdin", 1, offset, text))
    return tokens
