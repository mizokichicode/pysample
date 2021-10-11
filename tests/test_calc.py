import unittest
from pysample import calc

class TestCals(unittest.TestCase):

    def test_add(self):
        '''test method of calc.add()
        '''
        v1 = 10
        v2 = 8
        exp = 18
        act = calc.add(v1, v2)
        self.assertEqual(act, exp)


    def test_subtraction(self):
        '''test method of calc.subtraction()
        '''
        v1 = 10
        v2 = 8
        exp = 2
        act = calc.subtraction(v1, v2)
        self.assertEqual(act, exp)


    def test_multiplication(self):
        '''test method of calc.muliplication()
        '''
        v1 = 10
        v2 = 8
        exp = 80
        act = calc.multiplication(v1, v2)
        self.assertEqual(act, exp)


    def test_division(self):
        '''test method of calc.division()
        '''
        v1 = 10
        v2 = 8
        exp = 1
        act = calc.division(v1, v2)
        self.assertEqual(act, exp)