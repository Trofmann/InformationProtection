from typing import List

from utils import get_text_bits_list


class Coder(object):
    """Для случая с одним или двумя обычными пробелами"""
    separator = '\n'

    def __init__(self, key: str = ''):
        self.key = list(key.split(self.separator))  # type: List[str]

    def encode(self, msg: str) -> str:
        if not self.key or (len(self.key) == 1 and self.key[0] == ''):
            raise Exception('Для шифрования необходим контейнер')
        msg = get_text_bits_list(msg)  # Переводим сообщение в массив бит
        msg_len = len(msg)
        result = []
        msg_sym_ind = 0  # Указатель на бит, который надо вставить в контейнер
        for line in self.key:
            # Удаляем пробелы перед окончанием строки
            line = line.rstrip(' ')
            if msg_sym_ind == msg_len:
                # Сообщение полностью в контейнере
                continue

            if msg[msg_sym_ind]:
                # 1 Кодируется 1 пробелом
                result.append(line + ' ')
            else:
                # 0 Кодируется 2 пробелами
                result.append(line + ' ' * 2)
            msg_sym_ind += 1

        if msg_sym_ind != msg_len:
            return 'Сообщение не влезло в контейнер'
        return self.separator.join(result)

    def decode(self, msg: str) -> str:
        return ''
