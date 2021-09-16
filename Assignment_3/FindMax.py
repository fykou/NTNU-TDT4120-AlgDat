
#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
En unimodal liste er en liste med tall som, etter å ha blitt rotert et bestemt antall ganger, 
kan deles i to intervaller der det første er strengt voksende og det andre strengt synkende. 
Med rotasjon mener vi her å ta det første elementet ut av listen og sette det inn bak alle de andre elementene i listen.

Et eksempel er listen ⟨8,6,3,1,5,9,12,10⟩⟨8,6,3,1,5,9,12,10⟩. Hvis man roterer denne listen 3 ganger ender man opp med ⟨1,5,9,12,10,8,6,3⟩⟨1,5,9,12,10,8,6,3⟩, 
som har egenskapen at listen er først strengt voksende og deretter strengt synkende. ⟨8,6,3,1,5,9,12,10⟩⟨8,6,3,1,5,9,12,10⟩ er derfor en unimodal liste.

I en slik unimodal liste er det en bestemt største verdi. Du skal skrive en algoritme som finner denne verdien i Θ(lgn)Θ(lgn)-tid.
'''


import random
import sys

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(123)
 
 
def find_maximum(A):
    l = 0
    h = len(A) - 1
    i = 0
    while True:

        if l == h: 
            return A[l]
        
        #len == 2 and left is biggest
        if (h == l + 1 and A[l] >= A[h]): 
            return A[l] 

        #len == 2 and right is biggest
        if (h == l + 1 and A[l] < A[h]): 
            return A[h]


        mid = (l + h)//2
        if (A[mid] > A[mid + 1] and A[mid] > A[mid - 1]):
            return A[mid]
        elif (A[h] < A[l] and A[mid] < A[mid + 1] and A[l] < A[mid]): #1r ok
            l = mid
        elif A[h] < A[l] and ((A[mid] < A[mid + 1] and A[l] > A[mid]) or A[mid] > A[mid + 1]): #2l
            h = mid
        elif A[h] > A[l] and (A[mid] < A[l] or A[mid] < A[mid + 1]): #3r
            l = mid
        elif A[h] > A[l] and A[mid] > A[l] and A[mid] > A[mid + 1]: #4l
            h = mid
        else:
            l = mid


# Noen håndskrevne tester
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]


def generate_random_test_case(length, max_value):
    test = random.sample(range(max_value), k=length)
    m = max(test)
    test.remove(m)
    t = random.randint(0, len(test))
    test = sorted(test[:t]) + [m] + sorted(test[t:], reverse=True)
    t = random.randint(0, len(test))
    test = test[t:] + test[:t]
    return (test, m)


def test_student_maximum(test_case, answer):
    student = find_maximum(test_case)
    if student != answer:
        if len(test_case) < 20:
            response = (
                "'Find maximum' feilet for følgende input: "
                + "(x={:}). Din output: {:}. ".format(test_case, student)
                + "Riktig output: {:}".format(answer)
            )
        else:
            response = (
                "Find maximum' feilet på input som er "
                + "for langt til å vises her"
            )
        print(response)
        sys.exit()
    print(student, " - ", answer)


# Testing student maximum on custom made tests
for test_case, answer in tests:
    test_student_maximum(test_case, answer)

# Testing student maximum on random test cases
for i in range(40):
    test_case, answer = generate_random_test_case(random.randint(1, 10), 20)
    test_student_maximum(test_case, answer)