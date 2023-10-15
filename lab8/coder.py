from typing import List, Generator

from utils import get_text_bits_list, get_bit_list_text


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
        msg.append(0)  # Последний ноль - маркер окончания сообщения
        msg_len = len(msg)
        result = []
        msg_sym_ind = 0  # Указатель на бит, который надо вставить в контейнер

        for ind, sym in enumerate(self.key):
            # Очевидно, что текущий символ надо добавлять всегда
            result.append(sym)
            if ind == key_len - 1:
                # Конец контейнера
                continue
            if msg_sym_ind == msg_len:
                # Сообщение полностью в контейнере
                continue

            # Конец предложение и следующий символ пробел - место для внесения данных
            if sym in self.sentence_separators and self.key[ind + 1] == ' ':
                if not msg[msg_sym_ind]:
                    # Бит равен 0, добавим пробел
                    result.append(' ')
                # Сдвинем указатель
                msg_sym_ind += 1

        if msg_sym_ind != msg_len:
            return 'Сообщение не влезло в контейнер'
        return ''.join(result)

    def decode(self, msg: str) -> str:
        msg_len = len(msg)
        result = []  # type: List[int]
        result_str = []  # type: List[str]
        for ind, sym in enumerate(msg):
            if ind == msg_len - 1:
                continue
            if sym in self.sentence_separators:
                count_ = (msg[ind + 1] == ' ')  # Следующий символ - пробел
                if count_:
                    # Рассматриваем, только если следующий символ пробел
                    count_ += ((ind + 2 <= msg_len - 1) and msg[ind + 2] == ' ')  # Через символ тоже пробел
                    result.append(count_ % 2)

        # Вспоминаем про маркер окончания сообщения.
        # Добираем до последнего нуля
        while result[-1]:
            result.pop(-1)
        if result[-1] == 0:
            # И ноль тоже удаляем, т.к это маркер
            result.pop(-1)

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
