from des_mixin import DesMixin
from lab4 import Coder as Lab4Coder


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key
        self.des_coder = Lab4Coder(self.key)

    def encode(self, msg: str) -> str:
        result = []
        return ''.join(result)

    def decode(self, msg: str) -> str:
        result = []
        return ''.join(result)
