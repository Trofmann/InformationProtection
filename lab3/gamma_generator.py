from .const import A, B, C, T_0
from typing import Generator

class GammaGenerator(object):
    @classmethod
    def generate(cls, count_: int) -> list:
        result = [T_0]
        for _ in range(count_ - 1):  # 1 элемент уже есть
            next_elem = (A * result[-1] + C) % B
            result.append(next_elem)
        print(result)
        return result

    @classmethod
    def generate_new(cls, count_: int) -> Generator[int]:
        prev = None
        for _ in range(count_):
            # Для самомго первого
            if prev is None:
                prev = T_0
                yield T_0
            next_elem = (A * prev + C) % B
            prev = next_elem
            yield next_elem
