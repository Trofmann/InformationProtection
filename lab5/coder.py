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

    def decode(self, msg: str):
        pass
