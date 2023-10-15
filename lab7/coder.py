from des_mixin import DesMixin
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.k = 8
        self.des_coder = Lab4Coder(self.key)

    def encode(self, msg: str) -> str:
        result = []
        input_block = self.get_initial_gamma(8, self.k)

        for sym in msg:
            # Левые k бит открытого текст
            sym_bits = self.get_symbol_bit_list(sym)
            input_block_text = self.get_bit_list_text(input_block)

            # Шифрование входного блока
            encoded_input_block = self.des_coder.encode(input_block_text)
            encoded_input_block = self.get_text_bits_list(encoded_input_block)

            # k-битовый вектор помещается в k правых бит входного блока
            input_block = input_block[self.k::] + encoded_input_block[0:self.k]

            # Гаммирование
            output_block = self.lists_xor(sym_bits, encoded_input_block[0:self.k])

            result.append(self.get_bit_list_text(output_block))

        return ''.join(result)

    def decode(self, msg: str) -> str:
        result = []
        return ''.join(result)
