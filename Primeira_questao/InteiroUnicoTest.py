import unittest
from Primeira_questao import InteiroUnico


class Test_InteiroUnico(unittest.TestCase):

    def test_find_sigle_number(self):
        result = InteiroUnico.find_single_number("1 1 2 3 3 4 5 4 5")
        self.assertEqual(result, 2)


