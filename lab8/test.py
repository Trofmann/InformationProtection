import unittest

from lab8.coder import Coder


class TestLab8Coder(unittest.TestCase):
    def test_open_text_equals_decoded(self):
        key = '123'
        open_text = '1231414'
        coder = Coder(key)
        self.assertEqual(open_text, coder.decode(coder.encode(open_text)))
