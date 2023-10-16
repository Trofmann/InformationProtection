from typing import List, Generator

from utils import get_text_bits_list, get_bit_list_text


class Coder(object):
    """Для случая с обычным и неразрывным пробелом"""
    separator = '\n'
    space = ' '
    nbsp = chr(160)

    # 0 - обычным пробелом, 1 - неразрывным
    mapping = [space, nbsp]

    def __init__(self, key: str = '', count_: int = 2):
        self.key = list(key.split(self.separator))  # type:List[str]
        if count_ < 1:
            raise Exception('Количество кодируемых бит в строке должно быть не менее 1')
        self.count = count_

    def encode(self, msg: str) -> str:
        if not self.key or (len(self.key) and self.key[0] == ''):
            raise Exception('Для шифрования необходим контейнер')
        msg = get_text_bits_list(msg)
        msg_len = len(msg)
        result = []
        msg_sym_ind = 0  # Указатель на бит, который надо вставить в контейнер
        for line in self.key:
            line = line.rstrip(self.space + self.nbsp)

            if msg_sym_ind == msg_len:
                # Сообщение полностью в контейнере
                result.append(line)
                continue
            addition = ''
            # Кодируем count бит
            for _ in range(self.count):
                if msg_sym_ind == msg_len:
                    break
                msg_bit = msg[msg_sym_ind]
                addition = addition + self.mapping[msg_bit]
                msg_sym_ind += 1
            result.append(line + addition)

        if msg_sym_ind != msg_len:
            return 'Сообщение не влезло в контейнер'
        return self.separator.join(result)

    def decode(self, msg: str) -> str:
        result = []  # type: List[int]
        result_str = []  # type: List[str]

        for line in msg.split(self.separator):
            # Строка не заканчивается на один из пробелов, а значит больше нет строк с пробелами
            if line[-1] not in self.mapping:
                break
            addition = []

            for i in range(self.count):
                elem = line[-(i + 1)]
                # Текущий символ не пробельный, нет смысла проверять
                if elem not in self.mapping:
                    break
                addition.insert(0, self.mapping.index(elem))

            result.extend(addition)

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
