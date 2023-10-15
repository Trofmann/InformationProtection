class Coder(object):
    def __init__(self, key: str = ''):
        self.key = key  # Для дешифрования ключ не нужен
        self.sentence_separators = '.!?'

    def encode(self, msg: str) -> str:
        if not self.key:
            raise Exception('Для шифрования необходим контейнер')

        key_len = len(self.key)
        msg_len = len(msg)
        result = []
        msg_sym_ind = 0  # Индекс элемента, который надо вставить в контейнер

        for ind, sym in enumerate(self.key):
            # Очевидно, что текущий символ надо добавлять всегда
            result.append(sym)
            if ind == key_len - 1:
                # Конец контейнера
                continue
            if msg_sym_ind == msg_len - 1:
                # Сообщение полностью в контейнере
                continue

        if msg_sym_ind != msg_len - 1:
            return 'Сообщение не влезло в контейнер'
        return ''.join(result)

    def decode(self, msg: str) -> str:
        return ''
