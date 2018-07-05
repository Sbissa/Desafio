import unittest
from Segunda_questao import FlipBit


class Test_FlipBit(unittest.TestCase):

    def test_find_sigle_number(self):
        entry = [3, 2147483647, 1, 0]
        result = FlipBit.flip_bit(entry)
        self.assertEqual(result, [2147483648, 4294967294, 4294967295])
