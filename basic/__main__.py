import math
import pprint

import lexer
import parser


def print_traceback(text: str, error: SyntaxError) -> None:
    if error.offset is None:
        error.offset = len(text)
    print(f"stdin:1:{error.offset}: error: {error.msg}")
    print(f"\t1 |\t{text}")
    print(f"\t  |\t{' ' * (error.offset - 1)}^")


def main() -> None:
    while True:
        code = input("> ")
        try:
            tokens = lexer.lex(code)
            ast = parser.parse(tokens)
        except SyntaxError as error:
            print_traceback(code, error)
            continue
        pprint.pprint(tokens)
        pprint.pprint(ast)


if __name__ == "__main__":
    main()
