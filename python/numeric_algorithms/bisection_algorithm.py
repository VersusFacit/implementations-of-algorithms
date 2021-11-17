'''Implementation of finding the nth-root by bisection, with error'''

import math
import unittest


def nth_root(value, error=10**-12, n=2):
    '''Time O(log(n)) Aux. Space O(1)'''
    if n % 2 == 0 and value < 0:
        raise ValueError('Complex numbers not supported')

    if value >= 0:
        high = value
        low = 0
    else:
        high = 0
        low = value

    mid = (low + high) / 2
    while abs(value - mid**n) > error:
        if mid ** n > value:
            high = mid
        else:  # mid ** n < value:
            low = mid

        mid = (low + high) / 2
    return mid


class TestBisectionRoots(unittest.TestCase):
    def test_square_root_square(self):
        self.assertEqual(2.000, nth_root(4))

    def test_square_root_non_square(self):
        self.assertEqual(
            round(math.sqrt(3), 7),
            round(nth_root(3), 7)
        )

    def test_square_root_non_square_more_precision(self):
        self.assertEqual(
            round(math.sqrt(11), 10),
            round(nth_root(11), 10)
        )

    def test_square_root_zero(self):
        self.assertEqual(0, nth_root(0))

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            nth_root(-1)

    def test_cube_root_positive_cube(self):
        self.assertEqual(3, round(nth_root(27, n=3), 1))

    def test_cube_root_negative_cube(self):
        self.assertEqual(-1, round(nth_root(-1, n=3), 1))

    def test_cube_root_negative_noncube(self):
        self.assertEqual(
            round((-11**(1/3)), 10),
            round(nth_root(-11, n=3), 10)
        )

    def test_fourth_root_negative(self):
        with self.assertRaises(ValueError):
            nth_root(-16, n=4)

    def test_fifth_root_negative(self):
        self.assertEqual(
            round((-11**(1/5)), 10),
            round(nth_root(-11, n=5), 10)
        )
