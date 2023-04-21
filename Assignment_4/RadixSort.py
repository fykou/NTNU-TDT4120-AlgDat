#!/usr/bin/env python
__author__ = "Hoyby"

# incomplete

"""
Universitetet på Pluto ønsker også å sortere lister over studenter i leksikalsk rekkefølge. 
Det vil si slik at for eksempel «a» kommer før «b» og «aab» kommer før «ab», men etter «aa». 
Plutonske navn fungerer ikke slik som i Norge, og kan både være veldig korte (for eksempel «a»)eller veldig lange (mange tusener av tegn). 
Derfor er det ønskelig med en algoritme som sorterer en liste i lineær tid basert på den totale lengden til alle strengene og ikke som
en funksjon av den maksimale lengden til et navn. Plutonske navn kan også kun inneholde de små bokstavene fra og med «a» til og med «z».

Implementer en variant av RADIX-SORTRADIX-SORT som sorterer et sett med plutonske navn i leksikalsk rekkefølge.
Metoden skal ta inn en liste, A, og den maksimale lengden, k, et navn kan ha. 
Sorteringen må gå i lineær tid basert på den totale lengden til alle strengene.
"""


def char_to_int(char):
    return ord(char) - 97


BASE = 26  # Tallsystem (26): 0:a, 1:b ... 25:z


def flexradix(A, index):
    # Dersom lengden av A er mindre eller lik 1, returnerer jeg A
    if len(A) < 2:
        return A

    result = []
    # Lager 26 heaps
    heaps = [[] for base_number in range(BASE)]
    for string in A:
        # Dersom indexen er mindre eller lik lengden til strengen, legger jeg strengen til i resultater
        if index >= len(string):
            result.append(string)
        else:
            # Legger strengen til i en heap med tilhørende verdi(0-25) fra string[index] sin ASCII-verdi minus ASCII-verdien til 'a'
            heaps[ord(string[index]) - ord("a")].append(string)
    # Setter listen med hauger til å være en liste av ett nytt flexradix-kall på alle haugene
    heaps = [flexradix(heap, index + 1) for heap in heaps]

    # Legger til alle de resterende strengene i resultatlista med en dobbel for-løkke
    return result + [string for heap in heaps for string in heap]


# def counting_sort(A):
#     B = []
#     k = 2048

#     # Create empty list
#     C = [0] * k

#     # Store count of each number
#     for j in A:
#         C[j] += 1

#     # Cumulate C over the array
#     for i in range(1, len(C)):
#         C[i] += C[i - 1]

#     # Add to output array
#     for i in range(len(A) - 1, -1, -1):
#         B[C[A[i]] - 1] = A[i]
#         C[A[i]] -= 1
#     A = B


tests = (
    (([], 1), []),
    ((["a"], 1), ["a"]),
    ((["a", "b"], 1), ["a", "b"]),
    ((["b", "a"], 1), ["a", "b"]),
    ((["ba", "ab"], 2), ["ab", "ba"]),
    ((["b", "ab"], 2), ["ab", "b"]),
    ((["ab", "a"], 2), ["a", "ab"]),
    ((["abc", "b"], 3), ["abc", "b"]),
    ((["abc", "b"], 4), ["abc", "b"]),
    ((["abc", "b", "bbbb"], 4), ["abc", "b", "bbbb"]),
    ((["abcd", "abcd", "bbbb"], 4), ["abcd", "abcd", "bbbb"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
)

for test, solution in tests:
    student_answer = flexradix(test[0], test[1])
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )
