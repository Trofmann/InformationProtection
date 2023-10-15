from gamma_generator import GammaGenerator


class Coder(object):
    def __init__(self, key: str):
        self.key = key

    def encode(self, msg: str):
        pass

    def decode(self, msg: str):
        pass

    def _split_text_to_blocks(self, text: str):
        # Надо разбить текст на 64 битовые блоки. 1 символ 8 бит, значит на блоки по 8 символов
        pass
