from des_mixin import DesMixin
from gamma_generator import GammaGenerator
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.des_coder = Lab4Coder(self.key)

    def encode(self, msg: str):
        c = next(GammaGenerator().generate_new(1))  # Начальный вектор
        for block in self.split_text_to_blocks(msg):
            pass

    def decode(self, msg: str):
        pass
