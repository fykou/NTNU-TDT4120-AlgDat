#!/usr/bin/env python
__author__ = "Hoyby"

"""
Gitt en følge av tall, S=⟨s1,s2,…,sn⟩, ønsker vi å finne den lengste strengt synkende delfølgen (eller delsekvensen, subsequence) av SS. 
Vi ønsker å finne en slik S∗=⟨s∗1,s∗2,…,s∗k⟩ hvor kk er størst mulig.

Med en delfølge menes her en hvilken som helst følge som kan konstrueres ved å ta SS og eventuelt fjerne ett eller flere elementer. 
Det vil si at elementene må opptre i samme rekkefølge som i SS, men at ikke alle elementene fra SS trenger å finnes i delfølgen.

En følge, S=⟨s1,s2,…,sk⟩, kalles strengt synkende hvis si>si+1 gjelder for alle, i, hvor 0<i<k.

For eksempel la S=⟨8,7,3,6,2,5⟩. Da er S∗=⟨8,7,6,5⟩ en løsning på problemet vårt. Merk at S∗=⟨8,7,3,2⟩ og S∗=⟨8,7,6,2⟩ også er løsninger på problemet.

Problemet kan løses ved å teste alle mulige delfølger. Dette er en svært ineffektiv løsning, med eksponentiell kjøretid (Ω(2n)). 
Det er derimot effektivt å løse problemet med dynamisk programmering, som er det du skal gjøre i denne oppgaven. 
Det er mulig å løse problemet med både memoisering og iterasjon, men det kan være intuitivt lettere å bruke iterasjon.

Implementer funksjonen longest_decreasing_subsequence(s) som tar inn en følge, S, 
og returnerer den lengste strengt synkende delfølgen i S. Er det flere slike delfølger kan du returnere hvilken som helst av disse.
"""


def longest_decreasing_subsequence(s):
    # List containing lists with same lenght as s
    LDS = [[] for i in range(len(s))]
    # Set fist element
    LDS[0].append(s[0])

    for i in range(1, len(s)):
        for j in range(i):
            # find LDS that ends with s[j], but s[j] > s[i]
            if s[j] > s[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()

        LDS[i].append(s[i])

    j = 0
    for i in range(len(s)):
        if len(LDS[j]) < len(LDS[i]):
            j = i

    return LDS[j]


# Teste på formatet (følge, riktig lengde på svar)
tests = [
    ([1], 1),
    ([1, 2], 1),
    ([1, 2, 3], 1),
    ([2, 1], 2),
    ([3, 2, 1], 3),
    ([1, 3, 2], 2),
    ([3, 1, 2], 2),
    ([1, 1], 1),
    ([1, 2, 1], 2),
    ([8, 7, 3, 6, 2, 6], 4),
    ([10, 4, 2, 1, 7, 5, 3, 2, 1], 6),
    ([3, 7, 2, 10, 3, 3, 3, 9], 2),
]


def verify(sequence, subsequence, optimal_length):
    # Test if the subsequence is actually a subsequence
    index = 0
    for element in sequence:
        if element == subsequence[index]:
            index += 1
            if index == len(subsequence):
                break

    if index < len(subsequence):
        return False, "Svaret er ikke en delfølge av følgen."

    # Test if the subsequence is decreasing
    for index in range(1, len(subsequence)):
        if subsequence[index] >= subsequence[index - 1]:
            return False, "Den gitte delfølgen er ikke synkende."

    # Test if the solution is optimal
    if len(subsequence) != optimal_length:
        return (
            False,
            "Delfølgen har ikke riktig lengde. Riktig lengde er"
            + "{:}, mens delfølgen har lengde ".format(optimal_length)
            + "{:}".format(len(subsequence)),
        )

    return True, ""


failed = False

for test, optimal_length in tests:
    answer = longest_decreasing_subsequence(test[:])
    correct, error_message = verify(test, answer, optimal_length)

    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
