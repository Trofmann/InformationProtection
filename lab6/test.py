import unittest
from lab6.coder import Coder


class TestLab6Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        key = 'bafbbfgb'
        open_text = '123456789101112131415'
        coder = Coder(key=key)
        encoded = coder.encode(open_text)
        print(encoded)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)).rstrip(' '))
