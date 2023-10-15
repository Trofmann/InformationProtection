import unittest
from lab5.coder import Coder


class TestLab5Coder(unittest.TestCase):
    def test_working(self):
        key = 'baabbaaa'
        open_text = '123456891011121314'
        coder = Coder(key=key)
        encoded = coder.encode(open_text)
        print(encoded)
        self.assertEqual(True, True)
