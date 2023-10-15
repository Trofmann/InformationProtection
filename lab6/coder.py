from des_mixin import DesMixin
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.des_coder = Lab4Coder(self.key)
        self.k = 8

    def encode(self, msg: str) -> str:
        result = []
        # Начальный входной блок
        input_block = self.get_initial_gamma(8, self.k)

        for sym in msg:
            # Левые k бит открытого текста
            sym_bits = self.get_symbol_bit_list(sym)
            input_block_text = self.get_bit_list_text(input_block)
            # Шифрование входного блока
            encoded_input_block = self.des_coder.encode(input_block_text)
            encoded_input_block = self.get_text_bits_list(encoded_input_block)

            # Левые k бит результата шифрования гаммируются с левыми k битами открытого текст
            output_block = self.lists_xor(sym_bits, encoded_input_block[0:self.k])

            # k-битовый шифротекст поступает на дальнейшую обработку
            result.append(self.get_bit_list_text(output_block))

            # k-битовый вектор помещается в k правых бит входного блока
            input_block = input_block[self.k::] + output_block

        return ''.join(result)

    def decode(self, msg: str) -> str:
        result = []

        # Начальный входной блок
        input_block = self.get_initial_gamma(8, self.k)

        for sym in msg:
            # Левые k бит открытого текста
            sym_bits = self.get_symbol_bit_list(sym)

            # Шифрование входного текста
            decoded_input_block = self.des_coder.encode(self.get_bit_list_text(input_block))

            # Выходной блок
            output_block = self.get_text_bits_list(decoded_input_block)

            # левые k бит выходного блока
            output_block = output_block[0:self.k]

            # k бит открытого текст
            decoded_block = self.lists_xor(sym_bits, output_block)
            decoded_block = self.get_bit_list_text(decoded_block)
            result.append(decoded_block)

            # k бит шифротекста помещаются в k правых бит входного блока
            input_block = input_block[self.k::] + sym_bits

        return ''.join(result)
