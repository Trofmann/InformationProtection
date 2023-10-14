from typing import List

import const


def split_to_blocks(iterable: str, block_len: int) -> List[str]:
    return [iterable[i:i + block_len] for i in range(0, len(iterable), block_len)]


def get_char_code(c: str) -> int:
    return const.alphabet.index(c)


def get_code_char(code: int) -> str:
    return const.alphabet[code]
