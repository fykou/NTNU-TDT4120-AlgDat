#!/usr/bin/env python
__author__ = "Hoyby"

"""
Her skal du implementere MERGEMERGE og MERGE-SORTMERGE-SORT som beskrevet i læreboka.

Eneste forskjellen er at i din implementasjon er AA 0-indeksert siden AA er en liste i Python.
"""


import random
import math

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(123)


def merge(A, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = A[l + i]

    for j in range(0, n2):
        R[j] = A[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
    pass


def merge_sort(A, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        merge(A, l, m, r)
    pass


""" def generate_merge_tests():
    # Noen håndskrevne merge-tester
    tests = [
        (([1], 0, 0, 0), [1]),
        (([1, 3, 2], 0, 0, 1), [1, 3, 2]),
        (([3, 1, 2], 0, 0, 1), [1, 3, 2]),
        (([1, 2, 1, 2], 0, 1, 3), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 0, 1, 2), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 1, 1, 3), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 1, 1, 2), [1, 1, 2, 2]),
        (([1, 3, 1, 3, 1, 2, 4, 3], 2, 3, 6), [1, 3, 1, 1, 2, 3, 4, 3]),
        (
            ([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 0, 5),
            [2, 3, 4, 5, 6, 99, 7, 8, 7],
        ),
    ]

    # Noen tilfeldig-genererte merge-tester
    for i in range(10):
        p = random.randint(0, 5)
        q = p + random.randint(0, 5)
        r = q + random.randint(1, 5)
        test_case = (
            [random.randint(0, 10) for i in range(p)]
            + sorted([random.randint(0, 10) for i in range(q - p + 1)])
            + sorted([random.randint(0, 10) for i in range(r - q)])
            + [random.randint(0, 10) for i in range(random.randint(0, 5))],
            p,
            q,
            r,
        )
        answer = (
            test_case[0][:p]
            + sorted(test_case[0][p : r + 1])
            + test_case[0][r + 1 :]
        )
        tests.append((test_case, answer))

    return tests


# Tester merging
tests = generate_merge_tests()

for test_case, answer in tests:
    a, p, q, r = test_case
    student = a[:]
    merge(student, p, q, r)
    if student != answer:
        if len(a) < 20:
            response = (
                "Merge feilet for følgende input: "
                + "(a={:}, p={:}, q={:}, r={:}). ".format(a, p, q, r)
                + "Din output: {:}. Riktig output: {:}".format(student, answer)
            )
        else:
            response = "Merge feilet på input som er for langt til å vises her"
        print(response)
        break


def generate_merge_sort_tests():

    # Håndskrevne merge sort-tester
    tests = [
        (([], 0, -1), []),
        (([1], 0, 0), [1]),
        (([1, 3, 2], 0, 1), [1, 3, 2]),
        (([3, 1, 2], 0, 1), [1, 3, 2]),
        (([1, 2, 1, 2], 0, 3), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 0, 2), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 1, 3), [1, 1, 2, 2]),
        (([1, 2, 1, 2], 1, 2), [1, 1, 2, 2]),
        (([3, 1, 0, 5], 0, 3), [0, 1, 3, 5]),
        (([1, 3, 1, 3, 1, 2, 4, 3], 2, 6), [1, 3, 1, 1, 2, 3, 4, 3]),
        (([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 5), [2, 3, 4, 5, 6, 99, 7, 8, 7]),
        (([1, 0, 5], 7, 6), [1, 0, 5]),
        (([1, 0, 5], 7, 7), [1, 0, 5]),
        (([1, 0, 5], 1, 1), [1, 0, 5]),
    ]

    # Noen tilfeldige merge sort-tester
    for i in range(10):
        p = random.randint(0, 5)
        r = p + random.randint(0, 5)
        test_case = (
            [random.randint(0, 10) for i in range(r + random.randint(1, 5))],
            p,
            r,
        )
        answer = (
            test_case[0][:p]
            + sorted(test_case[0][p : r + 1])
            + test_case[0][r + 1 :]
        )
        tests.append((test_case, answer))

    return tests


tests = generate_merge_sort_tests()

# Tester mergesort
for test_case, answer in tests:
    a, p, r = test_case
    student = a[:]
    merge_sort(student, p, r)
    if student != answer:
        if len(a) < 20:
            response = (
                "Merge sort feilet for følgende input: "
                + "(a={:}, p={:}, r={:}). ".format(a, p, r)
                + "Din output: {:}. Riktig output: {:}".format(student, answer)
            )
        else:
            response = (
                "Merge sort feilet på input som "
                + "er for langt til å vises her"
            )
        print(response)
        break """
