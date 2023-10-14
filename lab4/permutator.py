from typing import List


class Permutator(object):
    def __init__(self, key: List[int]):
        self.key = key
        self.reverse_key = self.__get_reverse_key()

    def __get_reverse_key(self) -> List[int]:
        """Получение обратного ключа перестановки"""
        back_key = [0 for _ in range(len(self.key))]
        for ind, val in enumerate(self.key):
            back_key[val - 1] = ind
        return back_key

    def direct(self, list_: List[int]):
        return [list_[ind - 1] for ind in self.key]

    def reverse(self, list_: List[int]):
        return [list_[ind - 1] for ind in self.reverse_key]
