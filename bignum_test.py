""""
Module will test the functionality of functions in bignum.py.
Yvonne Cheng 
csci 112
Winter, 2023
"""

from bignum import Bignum

import unittest

class BignumTests(unittest.TestCase):

    def testInt(self):
        n = 2**100
        self. assertEqual (n, Bignum(n).int ())

    def testStr(self):
        bignum = (Bignum (20 ,8))
        self.assertEqual(str(bignum), "Bignum base 8: 4:2:+")
        bignum = (Bignum (20 ,2))
        self.assertEqual(str(bignum), "Bignum base 2: 0:0:1:0:1:+")
        bignum = (Bignum ( -123 ,10))
        self.assertEqual(str(bignum), "Bignum base 10: 3:2:1:-")
        bignum = (Bignum (50 ,16))
        self.assertEqual(str(bignum), "Bignum base 16: 2:3:+")

    def testAddition(self):
        n1 = 10
        n2 = 200
        bignum1 = Bignum(n1)
        bignum2 = Bignum(n2)
        result = bignum1 + bignum2
        solution = n1 + n2
        self.assertEqual(result.int(), solution)
                

if __name__ == '__main__':
    unittest.main(verbosity = 2)