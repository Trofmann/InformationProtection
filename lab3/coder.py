from gamma_generator import GammaGenerator
from utils import get_char_code, get_code_char
from . import const


class Coder(object):

    @staticmethod
    def encode(msg: str) -> str:
        codes = [get_char_code(c) for c in msg]  # Получаем коды символов сообщения
        result = []
        gamma_generator_ = GammaGenerator().generate_new(len(msg))  # Генератор гаммы
        for ind, gamma_val in zip(range(len(codes)), gamma_generator_):
            modified_code = (gamma_val + codes[ind]) % const.B  # Наложение гаммы
            result.append(get_code_char(modified_code))
        return ''.join(result)

    @staticmethod
    def decode(msg: str) -> str:
        codes = [get_char_code(c) for c in msg]  # Получаем коды символов сообщения
        result = []
        gamma_generator_ = GammaGenerator().generate_new(len(msg))  # Генератор гаммы
        for ind, gamma_val in zip(range(len(codes)), gamma_generator_):
            modified_code = codes[ind] - gamma_val
            if modified_code < 0:
                modified_code += const.B
            result.append(get_code_char(modified_code))
        return ''.join(result)
