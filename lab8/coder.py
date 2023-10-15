from utils import get_text_bits_list


class Coder(object):
    def __init__(self, key: str = ''):
        self.key = key  # Для дешифрования ключ не нужен
        self.sentence_separators = '.!?'
        self.__prepare_key()

    def __prepare_key(self):
        for elem in self.sentence_separators:
            old = f'{elem}  '
            new = f'{elem} '
            while old in self.key:
                self.key = self.key.replace(old, new)

    def encode(self, msg: str) -> str:
        if not self.key:
            raise Exception('Для шифрования необходим контейнер')

        key_len = len(self.key)
        msg = get_text_bits_list(msg)  # Переводим сообщение в массив бит
        msg.append(0)  # Последний ноль - маркер  окончания сообщения
        msg_len = len(msg)
        result = []
        msg_sym_ind = 0  # Указатель на бит, который надо вставить в контейнер

        for ind, sym in enumerate(self.key):
            # Очевидно, что текущий символ надо добавлять всегда
            result.append(sym)
            if ind == key_len - 1:
                # Конец контейнера
                continue
            if msg_sym_ind == msg_len - 1:
                # Сообщение полностью в контейнере
                continue

            # Конец предложение и следующий символ пробел - место для внесения данных
            if sym in self.sentence_separators and self.key[ind + 1] == ' ':
                if not msg[msg_sym_ind]:
                    # Бит равен 0, добавим пробел
                    result.append(' ')
                # Сдвинем указатель
                msg_sym_ind += 1

        if msg_sym_ind != msg_len - 1:
            return 'Сообщение не влезло в контейнер'
        return ''.join(result)

    def decode(self, msg: str) -> str:
        return ''
