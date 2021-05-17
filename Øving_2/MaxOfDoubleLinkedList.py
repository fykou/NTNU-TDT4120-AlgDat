#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
Finn det elementet med den høyeste veriden i en dobbelt linket liste.
'''


class NodeDoublyLinked:
    def __init__(self, prev_, next_, value):
        self.prev = prev_
        self.next = next_
        self.value = value

def maxOfDoubleLinkedList(linkedlist):
    start = linkedlist
    result = linkedlist.value
    if start.next != None:
        while linkedlist.next != None:
            if linkedlist.next.value > result:
                result = linkedlist.next.value 
            else:
                result = result
            linkedlist = linkedlist.next
    
    if start.prev != None:
        linkedlist = start
        while linkedlist.prev != None:
            if linkedlist.prev.value > result:
                result = linkedlist.prev.value
            else:
                result = result
            linkedlist = linkedlist.prev

    return result


#-------------------- Test --------------------

import unittest

n3 = NodeDoublyLinked(None, None, 100)
n2 = NodeDoublyLinked(None, n3, 10)
n1 = NodeDoublyLinked(None, n2, 1)

class Test(unittest.TestCase):
    def testset(self):
        self.assertEqual(maxOfDoubleLinkedList(n1), 100)
        self.assertEqual(maxOfDoubleLinkedList(n2), 100)
        self.assertEqual(maxOfDoubleLinkedList(n3), 100)

unittest.main()