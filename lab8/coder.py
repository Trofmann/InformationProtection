class Coder(object):
    def __init__(self, key: str = ''):
        self.key = key  # Для дешифрования ключ не нужен
        self.sentence_separators = '.!?'

    def encode(self, msg: str) -> str:
        if not self.key:
            raise Exception('Для шифрования необходим контейнер')
        result = []
        return ''.join(result)

    def decode(self, msg: str) -> str:
        return ''
