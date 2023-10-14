from utils import split_to_blocks

from . import const


class Coder(object):
    def __init__(self, key: dict):
        self.key = key
        self.back_key = self.get_back_key()

    def encode(self, msg: str) -> str:
        blocks = split_to_blocks(msg, const.BLOCK_LEN)
        return ''.join([self.key[block] for block in blocks])

    def decode(self, msg: str) -> str:
        blocks = split_to_blocks(msg, const.BLOCK_LEN)
        return ''.join([self.back_key[block] for block in blocks])

    def get_back_key(self) -> dict:
        back_key = dict()
        for key, value in self.key.items():
            back_key[value] = key
        return back_key
