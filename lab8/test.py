import unittest

from lab8.coder import Coder


class TestLab8Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        with open('key.txt', encoding='utf-8') as f:
            key = f.read()
        open_text = '1231414'
        coder = Coder(key)
        encoded = coder.encode(open_text)
        print(encoded)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)))
