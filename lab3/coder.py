from .gamma_generator import GammaGenerator
from utils import get_char_code, get_code_char
from . import const


class Coder(object):

    @staticmethod
    def encode(msg: str) -> str:
        gamma = GammaGenerator.generate(len(msg))  # Генерируем гамму
        codes = [get_char_code(c) for c in msg]  # Получаем коды символов сообщения
        result = []
        for ind in range(len(codes)):
            modified_code = (gamma[ind] + codes[ind]) % const.B  # Наложение гаммы
            result.append(get_code_char(modified_code))
        return ''.join(result)

    @staticmethod
    def decode(msg: str) -> str:
        gamma = GammaGenerator.generate(len(msg))  # Генерируем гамму
        codes = [get_char_code(c) for c in msg]  # Получаем коды символов сообщения
        result = []
        for ind in range(len(codes)):
            modified_code = codes[ind] - gamma[ind]
            if modified_code < 0:
                modified_code += const.B
            result.append(get_code_char(modified_code))
        return ''.join(result)
