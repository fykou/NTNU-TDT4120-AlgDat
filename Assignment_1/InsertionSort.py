#!/usr/bin/env python
__author__ = "Hoyby"

"""
Implementer sorteringsmetoden INSERTION-SORTINSERTION-SORT. 
Funksjonen din skal returnere den sorterte listen.

Merk: Det er ikke lov til å bruke innebygde funksjoner for sortering.
"""


def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


A = [4, 3, 2, 1]

print(insertionsort(A))
