#!/usr/bin/env python
__author__ = "Hoyby"

"""
Reverser listen og begrens den maksimale verdien til "maxnumber".
"""


def reverseAndLimit(array, maxnumber):
    result = deep(array)
    for i in range(0, len(array)):
        x = list.pop(array)
        if x > maxnumber:
            x = maxnumber

        result[i] = x

    return result


def deep(array):
    return array.copy()


# -------------------- Test --------------------

import unittest

array = [6, 5, 4, 3, 2, 1]


class Test(unittest.TestCase):
    def testset(self):
        self.assertEqual(reverseAndLimit(deep(array), 3), [1, 2, 3, 3, 3, 3])
        self.assertEqual(reverseAndLimit(deep(array), 4), [1, 2, 3, 4, 4, 4])
        self.assertEqual(reverseAndLimit(deep(array), 50), [1, 2, 3, 4, 5, 6])
        self.assertEqual(reverseAndLimit(deep(array), -1), [-1, -1, -1, -1, -1, -1])


unittest.main()
