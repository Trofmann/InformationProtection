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
            print()
        return ''

    def _encode_block(self, block: List[int]) -> List[int]:
        """Кодирование блока"""
        block = self._get_initial_block_permutation(block)

        left_part, right_part = block[0:32], block[32:64]
        for i in range(16):
            # 16 циклов шифрующих преобразований
            new_left_part = right_part
            key = self.keys[i]
            new_right_part = self._lists_xor(left_part, self._func_r_k(right_part, key))

            left_part = new_left_part
            right_part = new_right_part

        block = left_part + right_part
        block = self._get_reverse_block_permutation(block)
        return block

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

    def _func_r_k(self, r_part_block: List[int], key: List[int]):
        """f(R[i-1], k[i])"""
        # Расширение до 48 битов
        block = self._extend_block(r_part_block)
        # Гаммирование с ключом
        block = self._lists_xor(block, key)
        # Разбиение на 8 блоков по 6 бит
        parts = [block[i:i + 6] for i in range(0, len(block), 6)]

        # Новый 32-битный полублок
        block = []
        for ind, part in enumerate(parts):
            part_value = self._ss_transformation(ind, part)
            block.extend(part_value)
        return self._get_block_permutation(block)

    def _get_block_permutation(self, block: List[int]):
        permutation_key = [
            16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
        ]
        return [block[ind - 1] for ind in permutation_key]

    def _extend_block(self, r_part_block: List[int]) -> List[int]:
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
                result[pos - 1] = bit
        return result

    @staticmethod
    def _ss_transformation(ind: int, part: List[int]) -> List[int]:
        """SS-преобразование"""
        s1 = [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ]
        s2 = [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ]
        s3 = [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ]
        s4 = [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ]
        s5 = [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ]
        s6 = [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ]
        s7 = [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ]
        s8 = [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 13, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 5, 12, 9, 0, 3, 5, 5, 11],
        ]
        ss_key = [
            s1, s2, s3, s4, s5, s6, s7, s8
        ]
        k = int(f'{part[0]}{part[5]}', 2)
        l_ = int(f'{part[2]}{part[3]}{part[4]}{part[5]}', 2)
        res_dec = ss_key[ind][k][l_]
        res_bin = bin(res_dec)[2::]
        res_bin = res_bin.zfill(4)
        return list(map(int, res_bin))

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

    @staticmethod
    def _lists_xor(list_1: List[int], list_2: List[int]) -> List[int]:
        """Сложение по модулю 2 элементов списка"""
        result = []
        for el_1, el_2 in zip(list_1, list_2):
            result.append(el_1 ^ el_2)
        return result

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
            1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
        ]
        value = shift_key[ind]
        return key_part[value:] + key_part[:value]

    # endregion
