from const import A, B, C, T_0
from typing import Generator


class GammaGenerator(object):
    def generate_new(cls, count_: int) -> Generator[int, None, None]:
        prev = None
        for _ in range(count_):
            # Для самого первого
            if prev is None:
                prev = T_0
                res = T_0
            else:
                next_elem = (A * prev + C) % B
                prev = next_elem
                res = next_elem
            yield res
