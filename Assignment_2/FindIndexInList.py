#!/usr/bin/env python
__author__ = "Hoyby"

"""
Returner verdien til elementet på den gitte indexen I en linket liste.
"""


import random


class Node:
    def __init__(self, next_, value_):
        super().__init__()
        self.next = next_
        self.value = value_


def createLinkedList(length):
    child = None
    node = None

    for i in range(0, length):
        node = Node(child, random.randint)
    return node


def findIndexInList(linkedlist, index):
    result = linkedlist

    if index == 1:
        return result.value

    for i in range(1, index):
        result = result.next
        if result == None:
            return -1

    return result.value


# -------------------- Test --------------------

import unittest

n3 = Node(None, 100)
n2 = Node(n3, 10)
n1 = Node(n2, 1)


class Test(unittest.TestCase):
    def testset(self):
        self.assertEqual(findIndexInList(n1, 1), 1)
        self.assertEqual(findIndexInList(n1, 2), 10)
        self.assertEqual(findIndexInList(n1, 3), 100)
        self.assertEqual(findIndexInList(n1, 4), -1)
        self.assertEqual(findIndexInList(n1, 50), -1)


unittest.main()
