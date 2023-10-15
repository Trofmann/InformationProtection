from typing import List

from des_mixin import DesMixin
from gamma_generator import GammaGenerator
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.des_coder = Lab4Coder(self.key)

    def encode(self, msg: str) -> str:
        c = next(GammaGenerator().generate_new(1))  # Начальный вектор
        c = self.get_int_bit_list(c, 64)
        result = []
        for block in self.split_text_to_blocks(msg):
            if result:
                # Не первая итерация, надо перегенерировать с
                c = self.get_text_bits_list(result[-1])
            block = self.get_text_bits_list(block)
            block = self.lists_xor(block, c)
            block = self.get_bit_list_text(block)
            encoded_block = self.des_coder.encode(block)
            result.append(encoded_block)
        return ''.join(result)

    def decode(self, msg: str) -> str:
        c = next(GammaGenerator().generate_new(1))
        # Предыдущий зашифрованный блок
        prev_encoded_block = self.get_int_bit_list(c, 64)  # type: List[int]
        # Результат
        result = []
        for block in self.split_text_to_blocks(msg):
            # Mi + 1 = Ci xor DES-1(K, Ci + 1).
            decoded_block = self.des_coder.decode(block)  # DES-1(K, Ci + 1)
            decoded_block_bits_list = self.get_text_bits_list(decoded_block)
            decoded_block = decoded_block_bits_list
            decoded_block = self.lists_xor(prev_encoded_block, decoded_block)  # Ci xor DES-1(K, Ci + 1)
            decoded_block = self.get_bit_list_text(decoded_block)  # Mi + 1
            result.append(decoded_block)

            prev_encoded_block = decoded_block_bits_list

        return ''.join(result)
