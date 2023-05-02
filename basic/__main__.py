#!/usr/bin/env python3

import os
from pprint import pprint

from lexer import Lexer, LexingError, Token
from parser import BinaryOperationNode, Parser, ParsingError

CODE_MESSAGE = "Code"
TOKEN_MESSAGE = "Tokenization"
PARSE_MESSAGE = "Abstract Syntax Tree"


def print_label(size: os.terminal_size, label: str) -> None:
    separator = "=" * (size.columns // 2 - len(label) // 2 - 1)
    print(f"{separator} {label} {separator}")



def get_code(size: os.terminal_size) -> str:
    code = input("> ")
    print_label(size, CODE_MESSAGE)
    print(code)
    return code


def tokenize(code: str, size: os.terminal_size) -> list[Token] | None:
    lexer = Lexer(code)
    try:
        tokens = lexer.tokens()
    except LexingError as e:
        print(e)
        return
    print_label(size, TOKEN_MESSAGE)
    print(tokens)
    return tokens


def parse(tokens: list[Token]) -> BinaryOperationNode | None:
    parser = Parser(tokens)
    try:
        return parser.ast()
    except ParsingError as e:
        print(e)


def main() -> None:
    terminal_size = os.get_terminal_size()

    while True:
        code = input("> ")
        if code == "quit":
            break
        print(code)

        print("=" * 16)

        tokens = tokenize(code)
        if tokens is None:
            continue
        print(tokens)

        print("=" * 16)

        tree = parse(tokens)
        if tree is None:
            continue
        print(tree)


if __name__ == "__main__":
    main()
