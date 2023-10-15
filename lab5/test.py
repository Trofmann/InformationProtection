import unittest
from lab5.coder import Coder


class TestLab5Coder(unittest.TestCase):
    def test_working(self):
        key = 'aaabeaaf'
        open_text = '123456789101112131415'
        coder = Coder(key=key)
        encoded = coder.encode(open_text)
        print(encoded)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)).rstrip(' '))

