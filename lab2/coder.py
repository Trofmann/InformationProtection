from utils import split_to_blocks
from . import const


class Coder(object):
    def __init__(self, key: list):
        self.key = key
        self.back_key = self.get_back_key()

    def _encode_block(self, block: str) -> str:
        res = []
        for i in range(len(block)):
            res.append(block[self.key[i]])
        return ''.join(res)

    def encode(self, msg: str) -> str:
        blocks = split_to_blocks(msg, const.BLOCK_LEN)
        return ''.join([self._encode_block(block) for block in blocks])

    def _decode_block(self, block: str) -> str:
        res = []
        for i in range(len(block)):
            res.append(block[self.back_key[i]])
        return ''.join(res)

    def decode(self, msg: str) -> str:
        blocks = split_to_blocks(msg, const.BLOCK_LEN)
        return ''.join([self._decode_block(block) for block in blocks])

    def get_back_key(self) -> list:
        back_key = [0 for _ in range(len(self.key))]
        for ind, val in enumerate(self.key):
            back_key[val] = ind
        return back_key
