#!/usr/bin/env python3

import pprint
from lexer import Lexer, LexError

while True:
    code = input("> ")
    if code == "quit":
        break
    try:
        tokens = Lexer(code).tokens()
    except LexError as e:
        print(e)
        continue
    pprint.pprint(tokens)
