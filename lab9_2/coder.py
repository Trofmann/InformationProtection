class Coder(object):
    """Для случая с обычным и неразрывным пробелом"""
    def __init__(self, key: str = '', count_: int = 2):
        self.key = key
        if count_ < 1:
            raise Exception('Количество кодируемых бит в строке должно быть не менее 1')
        self.count = count_

    def encode(self, msg: str) -> str:
        return ''

    def decode(self, msg: str) -> str:
        return ''
