from typing import List, Generator

from gamma_generator import GammaGenerator
from utils import (
    get_int_bit_list, get_symbol_bit_list, get_text_bits_list, get_bit_list_text
)


class DesMixin(object):
    """Вспомогательные функции для des"""

    @staticmethod
    def get_symbol_bit_list(symbol: str) -> List[int]:
        """Преобразование символа в массив битов"""
        return get_symbol_bit_list(symbol)

    def split_text_to_blocks(self, msg: str) -> Generator[str, None, None]:
        """Разбиение текста на блоки по 64 бита"""
        # Заметим, что 1 символ == 1 байт, значит, надо разбить на блоки по 8 символов

        # В случае нехватки дополним пробелами в конце
        block_len = 8
        need = len(msg) % block_len
        if need:
            msg = msg + ' ' * (8 - need)

        result = []
        for ind, sym in enumerate(msg):
            # Начало блока
            if ind % block_len == 0:
                result = []

            result.append(sym)

            # Это был последний символ блока, можем вернуть блок
            if ind % block_len == block_len - 1:
                yield ''.join(result)

    def get_text_bits_list(self, text: str) -> List[int]:
        """Текст в список битов"""
        return get_text_bits_list(text)

    @staticmethod
    def lists_xor(list_1: List[int], list_2: List[int]) -> List[int]:
        """Сложение по модулю 2 элементов списка"""
        result = []
        for el_1, el_2 in zip(list_1, list_2):
            result.append(int(bool(el_1) != bool(el_2)))
        return result

    @staticmethod
    def get_bit_list_text(list_: List[int]) -> str:
        """Перевод списка бит в строку"""
        return get_bit_list_text(list_)

    def get_initial_gamma(self, elem_count: int, elem_len: int) -> List[int]:
        result = []
        for num in GammaGenerator().generate_new(elem_count):
            result.extend(get_int_bit_list(num, elem_len))
        return result
