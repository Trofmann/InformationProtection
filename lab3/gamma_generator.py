from .const import A, B, C, T_0


class GammaGenerator(object):
    @classmethod
    def generate(cls, count_: int) -> list:
        result = [T_0]
        for _ in range(count_ - 1):  # 1 элемент уже есть
            next_elem = (A * result[-1] + C) % B
            result.append(next_elem)
        print(result)
        return result
