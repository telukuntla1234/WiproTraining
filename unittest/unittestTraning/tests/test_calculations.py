import sys
import unittest

from src.calculations import add, sub, mul, div, ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(n1=10 , n2=5)
        self.assertEqual(15, res, msg='Addition Error')

    def test_sub(self):
        res = sub(n1=10 ,n2=5)
        self.assertEqual(res, 5, msg='Subtraction Error')

    def test_mul(self):
        res = mul(n1=10 , n2=5)
        self.assertEqual(50,res, msg='Multiplication Error')

    def test_div(self):
        res = div(n1=10 , n2=5)
        self.assertEqual(2.0,res, msg='Division    Error')

    @unittest.skipIf(sys.version_info <= (3, 13), reason='Not Implemented yet')
    def test_ne(self):
        res = ne(n1=10, n2=10)
        self.assertTrue(res, msg='NE')

    def test_diverr(self):
        with self.assertRaises(ZeroDivisionError, msg='No Exception'):
            div(n1=10, n2=0)