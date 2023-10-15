import unittest
from lab4.coder import Coder


class TestLab4Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        key = 'baabbaaa'
        coder = Coder(key)
        open_text = '1234567891011121314'
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)).rstrip(' '))
