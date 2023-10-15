from typing import List

from des_mixin import DesMixin
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.des_coder = Lab4Coder(self.key)

    def encode(self, msg: str) -> str:
        prev_c = self.get_initial_gamma(8, 8)  # type: List[int]
        result = []
        for block in self.split_text_to_blocks(msg):
            block = self.get_text_bits_list(block)
            block = self.lists_xor(block, prev_c)
            prev_c = block
            block = self.get_bit_list_text(block)
            encoded_block = self.des_coder.encode(block)
            result.append(encoded_block)
        return ''.join(result)

    def decode(self, msg: str) -> str:
        # Предыдущий зашифрованный блок
        prev_encoded_block = self.get_initial_gamma(8, 8)
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
