#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
Ved universitetet på Pluto har hvert emne sin egen karakterskala. For et gitt emne består karakterskalaen av alle heltall ii, 
slik at 0⩽i⩽k0⩽i⩽k. Administrasjonen ved universitetet ønsker å sortere karakterene i emnene, 
slik at de lettere kan utføre statistiske utregninger. 
Dessverre kjenner ikke administrasjonen til verdien for kk for hvert enkelt emne,
de vet kun at denne verdien alltid er slik at k<2048k<2048.

Implementer en variant av COUNTING-SORTCOUNTING-SORT som ikke tar inn kk, 
men som alltid vil kunne sortere en liste av karakterer i et emne ved universitetet på Pluto. 
Metoden skal skrive resultatet til BB, som har lik lengde som AA.
'''


def counting_sort(A, B):
    k = 2048

    # Create empty list
    C = [0] * k
    
    # Store count of each number
    for j in A:
        C[j] += 1

    # Cumulate C over the array
    for i in range(1, len(C)):
        C[i] += C[i - 1]


    # Add to output array
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1


tests = (
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 1, 2, 1], [1, 1, 1, 2]),
    ([0, 1281, 1, 2], [0, 1, 2, 1281]),
    (
        [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
        [274, 303, 334, 488, 502, 546, 568, 709, 756, 995, 997, 999],
    ),
    (
        [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
        [50, 116, 253, 298, 356, 373, 568, 603, 648, 681, 772, 795],
    ),
)

for test, solution in tests:
    student_answer = [0] * len(test)
    counting_sort(test, student_answer)
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )