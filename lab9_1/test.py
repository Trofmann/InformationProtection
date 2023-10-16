import unittest
from lab9_1.coder import Coder


class TestLab91Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        with open('key.txt', encoding='utf-8') as f:
            key = f.read()
        open_text = '123141'
        coder = Coder(key)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)))
