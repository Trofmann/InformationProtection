from typing import Generator, List

from utils import get_char_code


class Coder(object):

    def __init__(self, key):
        if len(key) != 8:
            raise Exception('Длина ключа должна быть равна 8')
        self.keys = self._get_keys(key)

    # region Кодирование
    def encode(self, msg: str) -> str:
        for block in self.split_text_to_blocks(msg):
            encoded_block = self._encode_block(block)
        return ''

    def _encode_block(self, block: List[int]):
        """Кодирование блока"""
        block = self._get_initial_block_permutation(block)

        for i in range(16):
            # 16 циклов шифрующих преобразований
            pass

        block = self._get_reverse_block_permutation(block)

    def _get_initial_block_permutation(self, block: List[int]) -> List[int]:
        """Начальная перестановка"""
        # Индекс - IP[i], Значение - OT[i]
        # OT[i] - i-й бит входного блока, IP[i] - i-бит выходного блока
        key = [
            58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
        ]
        return [block[ind - 1] for ind in key]

    def _get_reverse_block_permutation(self, block: List[int]) -> List[int]:
        """Обратная перестановка"""
        key = [
            40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25,
        ]
        return [block[ind - 1] for ind in key]

    def _func_r_k(self, r_part_block: List[int]):
        """f(R[i-1], k[i])"""
        extended_block = self._extend_block(r_part_block)

    def _extend_block(self, r_part_block: List[int]):
        """Расширение 32-битного блока до 48 бит"""
        key = [
            [2, 48], [3], [4], [5, 7], [6, 8], [9], [10], [11, 13], [12, 14], [15], [16], [17, 19], [18, 20], [21],
            [22], [23, 35],
            [24, 26], [27], [28], [29, 31], [30, 32], [33], [34], [35, 37], [36, 38], [39], [40], [41, 43], [42, 44],
            [45], [46], [1, 47]
        ]
        result = [0 for _ in range(48)]
        for ind, bit in enumerate(r_part_block):
            positions = key[ind]
            for pos in positions:
                result[pos] = bit
        return result

    # endregion

    # region Декодирование
    def decode(self, msg: str) -> str:
        return ''

    # endregion

    # region Вспомогательные функции
    @staticmethod
    def _get_symbol_byte_list(symbol: str) -> List[int]:
        """Преобразование символа в массив битов"""
        code = get_char_code(symbol)
        code_str = bin(code)[2::]
        code_str = code_str.zfill(8)
        return list(map(int, code_str))

    def split_text_to_blocks(self, msg: str) -> Generator[List[int], None, None]:
        """Разбиение текста на блоки по 64 бита"""
        # Заметим, что 1 символ == 1 байт, значит, надо разбить на блоки по 8 символов
        # Для удобства же сразу будем возвращать список битов

        # В случае нехватки дополним пробелами в конце
        block_len = 8
        need = len(msg) % block_len
        if need:
            msg = msg + ' ' * need

        result = []
        for ind, sym in enumerate(msg):
            # Начало блока
            if ind % block_len == 0:
                result = []

            result.extend(self._get_symbol_byte_list(sym))

            # Это был последний символ блока, можем вернуть блок
            if ind % block_len == block_len - 1:
                yield result

    # endregion

    # region Ключи
    def _get_keys(self, key_txt: str) -> List[List[int]]:
        """
        Получение ключей
        :param key_txt: введённый ключ
        :return:
        """
        key = []  # type: List[int]  # Ключ в виде массива битов
        keys = []  # type: List[List[int]]
        for sym in key_txt:
            key.extend(self._get_symbol_byte_list(sym))
        key = self._get_key_permutation_1(key)

        key_left_part, key_right_part = key[0:28], key[28:56]

        for i in range(16):
            key_left_part = self._key_part_cyclic_left_shift(key_left_part, i)
            key_right_part = self._key_part_cyclic_left_shift(key_right_part, i)
            key = key_left_part + key_right_part
            key = self._get_key_permutation_2(key)
            keys.append(key)

        return keys

    @staticmethod
    def _get_key_permutation_1(key: List[int]) -> List[int]:
        """Перестановка-выбор 1"""
        permutation_key = [
            57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
        ]
        return [key[ind - 1] for ind in permutation_key]

    @staticmethod
    def _get_key_permutation_2(key: List[int]) -> List[int]:
        """Перестановка-выбор 2"""
        permutation_key = [
            14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
        ]
        return [key[ind - 1] for ind in permutation_key]

    @staticmethod
    def _key_part_cyclic_left_shift(key_part: List[int], ind: int) -> List[int]:
        """Циклический сдвиг влево части ключа"""
        shift_key = [
            1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1
        ]
        value = shift_key[ind]
        return key_part[value:] + key_part[:value]

    # endregion
