from des_mixin import DesMixin


class Coder(DesMixin):
    def __init__(self, key: str):
        self.key = key

    def encode(self, msg: str):
        pass

    def decode(self, msg: str):
        pass
