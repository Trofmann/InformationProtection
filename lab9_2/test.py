import unittest
from lab9_2.coder import Coder


class TestLab92Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        with open('key.txt', encoding='utf-8') as f:
            key = f.read()
        open_text = '123141'
        coder = Coder(key)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)))
