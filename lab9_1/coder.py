from typing import List, Generator

from utils import get_text_bits_list, get_bit_list_text


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
                result.append(line)
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
        result = []  # type: List[int]
        result_str = []  # type: List[str]

        for line in msg.split(self.separator):
            # Строка не заканчивается на пробел, а значит больше нет строк с пробелами
            if line[-1] != ' ':
                break
            count_ = (line[-1] == ' ') + (line[-2] == ' ')
            # 0 Кодируется 2 пробелами, 1 - 1 пробелом
            result.append(count_ % 2)

        for block in self._split_to_blocks(result):
            block = get_bit_list_text(block)
            result_str.append(block)
        return ''.join(result_str)

    def _split_to_blocks(self, list_: List[int], block_len=8) -> Generator[List[int], None, None]:
        block = []
        for elem in list_:
            block.append(elem)
            if len(block) == block_len:
                temp = block
                block = []
                yield temp
