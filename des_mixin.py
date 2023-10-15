from typing import List, Generator

from utils import get_char_code, split_to_blocks, get_code_char


class DesMixin(object):
    """Вспомогательные функции для des"""

    @staticmethod
    def get_symbol_bit_list(symbol: str) -> List[int]:
        """Преобразование символа в массив битов"""
        code = get_char_code(symbol)
        return DesMixin.get_int_bit_list(code, len_=8)

    @staticmethod
    def get_int_bit_list(num: int, len_=8) -> List[int]:
        num_str = bin(num)[2::]
        num_str = num_str.zfill(len_)
        return list(map(int, num_str))

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
        result = []
        for sym in text:
            result.extend(self.get_symbol_bit_list(sym))
        return result

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
        parts = split_to_blocks(list_, 8)
        result = []
        for part in parts:
            bin_str = ''.join(map(str, part))
            symbol_code = int(bin_str, 2)
            result.append(get_code_char(symbol_code))
        return ''.join(result)
