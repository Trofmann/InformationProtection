import unittest
from lab4.coder import Coder


class TestLab4Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        key = 'baabbaaa'
        open_text = '123456891011121314'
        coder = Coder(key)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)).rstrip(' '))
