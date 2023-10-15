import unittest

from lab7.coder import Coder


class TestLab7Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        key = 'dhsgahsg'
        open_text = '123456789101112131415'
        coder = Coder(key=key)
        encoded = coder.encode(open_text)
        print(encoded)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)).rstrip(' '))
