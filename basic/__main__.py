import pprint

import lexer


def print_traceback(error: SyntaxError) -> None:
    assert error.text is not None
    assert error.offset is not None

    print(f"stdin:1: syntax error near '{error.text[error.offset - 1]}'")


def main() -> None:
    while True:
        code = input("> ")
        try:
            pprint.pprint(lexer.lex(code))
        except SyntaxError as error:
            print_traceback(error)


if __name__ == "__main__":
    main()
