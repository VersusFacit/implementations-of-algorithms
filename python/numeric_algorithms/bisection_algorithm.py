'''Implementation of finding the squareroot by bisection, with error'''

import math
import unittest


def square_root(value, error=10**-12):
    '''Time O(log(n)) Aux. Space O(1)'''
    if value < 0:
        raise ValueError('Complex numbers not supported')

    high = value
    low = 0
    mid = (low + high) / 2
    while abs(value - mid**2) > error:
        if mid ** 2 > value:
            high = mid
        else:  # mid ** 2 < value:
            low = mid

        mid = (low + high) / 2
    return mid


class TestBisectionSquareRoot(unittest.TestCase):
    def test_square_root_square(self):
        self.assertEqual(2.000, square_root(4))

    def test_square_root_non_square(self):
        self.assertEqual(
            round(math.sqrt(3), 7),
            round(square_root(3), 7)
        )

    def test_square_root_non_square_more_precision(self):
        self.assertEqual(
            round(math.sqrt(11), 10),
            round(square_root(11), 10)
        )

    def test_square_root_zero(self):
        self.assertEqual(0, square_root(0))

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)
