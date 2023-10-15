from typing import List

import const


def split_to_blocks(iterable, block_len: int) -> List[str]:
    return [iterable[i:i + block_len] for i in range(0, len(iterable), block_len)]


def get_char_code(c: str) -> int:
    return const.alphabet.index(c)


def get_code_char(code: int) -> str:
    return const.alphabet[code]


def get_int_bit_list(num: int, len_=8) -> List[int]:
    """Преобразование числа в список бит"""
    num_str = bin(num)[2::]
    num_str = num_str.zfill(len_)
    return list(map(int, num_str))


def get_symbol_bit_list(symbol: str) -> List[int]:
    """Преобразование символа в массив битов"""
    code = get_char_code(symbol)
    return get_int_bit_list(code, len_=8)


def get_text_bits_list(text: str) -> List[int]:
    """Текст в список битов"""
    result = []
    for sym in text:
        result.extend(get_symbol_bit_list(sym))
    return result


def get_bit_list_text(list_: List[int]) -> str:
    """Перевод списка бит в строку"""
    parts = split_to_blocks(list_, 8)
    result = []
    for part in parts:
        bin_str = ''.join(map(str, part))
        symbol_code = int(bin_str, 2)
        result.append(get_code_char(symbol_code))
    return ''.join(result)
