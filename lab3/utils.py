from . import const


def get_char_code(c: str) -> int:
    return const.alphabet.index(c)


def get_code_char(code: int) -> str:
    return const.alphabet[code]
