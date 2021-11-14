# Given a sorted array of n integers and a target value, determine if the
# target exists in the array. If target exists in the array, print its index.

# Time Complexity:
#   Ω (1)           Target is the midpoint element.
#   O(log(n))       Search space halves on each iteration.
#   AVG_O(log(n))   About log(n) - 1; ~50% of outcomes before last iteration
# Auxiliary Space: O(log(n)) because of stack frames

import unittest


def binary_search(arr, target):
    '''deal with edge cases before loop over list'''
    def loop(low, high):
        '''tail recursive to support arbitrary depth if enabled'''
        if high < low:
            raise ValueError(f'Value {target} not found')

        curr = (low + high) // 2
        if arr[curr] > target:
            return loop(low, curr - 1)
        elif arr[curr] < target:
            return loop(curr + 1, high)
        else:
            return curr

    return loop(0, len(arr) - 1)


class TestBinarySearch(unittest.TestCase):
    '''test base cases'''
    def test_binary_search_base_cases(self):
        list1 = []
        target1 = 1
        with self.assertRaises(ValueError):
            binary_search(list1, target1)

        list2 = [1]
        target2 = 1
        self.assertEqual(0, binary_search(list2, target2))

    '''test more complicated lists, including ones with negative numbers'''
    def test_binary_search(self):
        list1 = list(range(100))
        target1 = 7
        self.assertEqual(
                list1.index(target1), binary_search(list1, target1))
        target1b = 51
        self.assertEqual(
            list1.index(target1b), binary_search(list1, target1b)
        )
        target1c = 16
        self.assertEqual(
            list1.index(target1c), binary_search(list1, target1c)
        )

        list2 = [1, 5, 10, 11, 16, 35, 100, 300]
        target2 = 10
        self.assertEqual(
            list2.index(target2), binary_search(list2, target2)
        )

        list3 = [-100, -123, -1, 5, 10, 11, 16, 35, 100, 300]
        target3 = -1
        self.assertEqual(
            list3.index(target3), binary_search(list3, target3)
        )

    '''test for numeric lists that are missing target value'''
    def test_binary_search_missing(self):
        list1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        target1 = 4
        with self.assertRaises(ValueError):
            binary_search(list1, target1)

        list2 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
        target2 = 5
        with self.assertRaises(ValueError):
            binary_search(list2, target2)

        list3 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
        target3 = -1
        with self.assertRaises(ValueError):
            binary_search(list3, target3)
