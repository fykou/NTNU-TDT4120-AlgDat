#!/usr/bin/env python
__author__ = "Hoyby"

# incomplete

"""
Du er i et basseng fylt med vann. Bassenget har en bunn som er flislagt med identiske kvadratiske fliser med sidelengde på 1 meter. 
Bassenget er helt kvadratisk med nn fliser i lengden og nn fliser i bredden. Dette er likevel ikke et helt vanlig basseng, 
fordi flisene ikke nødvendigvis ligger i samme dybde under vannflaten.

Du ønsker å gjemme en kiste i bassenget slik at hele kisten ligger under vannflaten (toppen kan være akkurat på vannflaten). 
Du har ikke laget kisten enda, men har bestemt at kisten skal ha form som et rett rektangulært prisme (et prisme der alle sider er rektangler). 
Kisten skal også ligge parallelt med flisene.

Det finnes flere slike basseng, og du ønsker å finne største mulige kiste i volum for hvert av bassengene. 
For å gjøre det enklere for deg selv, så skal du ikke regne ut dette for hånd; 
du skal skrive en algoritme som finner dette volumet for deg.

Input til algoritmen er en todimensjonal liste med dybde under vannflaten til flisene i meter.

Algoritmen din må ha O(n^4) som gjennomsnittlig kjøretid for å få godkjent.

Eksempel: Hvis listen du får inn er [[1, 1], [2, 1]], vil dette tilsvare et basseng som er slik:

(bilde av 2x2 baseng)

Her ser man at høyden på kisten kan være maksimum 2 meter siden siden det er det dypeste punktet i bassenget. 
Hvis kisten skal være 2 meter høy kan den kun ligge på den flisa som er på 2 meter dybde, 
noe som gir et volum på 1m⋅1m⋅2m=2m^3.

Hvis vi derimot har en kiste som er 1 meter høy, kan den ligge oppå alle flisene, 
siden alle flisene ligger minst en meter under vannoverflaten. Da får vi en kiste med volum 2m⋅2m⋅1m=4m^3.
Størrelsen på det størst mulige volumet i dette eksempelet er dermed 4m^3.
"""


import random
import base64
import sys

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(123)

# Minimalisert kode for å verifisere at svaret er riktig. Kan ignoreres.
exec(
    base64.b64decode(
        "ZGVmIGExMjMoeCx4MCx5MCx4MSx5MSk6Cg"
        + "lBPWZsb2F0KCdpbmYnKQoJZm9yIEIgaW4g"
        + "cmFuZ2UoeDAseDErMSk6CgkJZm9yIEMgaW"
        + "4gcmFuZ2UoeTAseTErMSk6QT1taW4oQSx4"
        + "W0JdW0NdKQoJcmV0dXJuIEEKZGVmIGJydX"
        + "RlZm9yY2UoeCk6CglBPTAKCWZvciBCIGlu"
        + "IHJhbmdlKGxlbih4KSk6CgkJZm9yIEMgaW"
        + "4gcmFuZ2UobGVuKHhbMF0pKToKCQkJZm9y"
        + "IEQgaW4gcmFuZ2UoQixsZW4oeCkpOgoJCQ"
        + "kJZm9yIEUgaW4gcmFuZ2UoQyxsZW4oeFsw"
        + "XSkpOkE9bWF4KEEsKEQtQisxKSooRS1DKz"
        + "EpKmExMjMoeCxCLEMsRCxFKSkKCXJldHVybiBB"
    )
)


def largest_cuboid(x):
    # Skriv koden din her
    pass


# Some håndskrevne tester
tests = [
    ([[1]], 1),
    ([[1, 1], [2, 1]], 4),
    ([[1, 1], [5, 1]], 5),
    ([[0, 0], [0, 0]], 0),
    ([[10, 0], [0, 10]], 10),
    ([[10, 6], [5, 10]], 20),
    ([[100, 100], [40, 55]], 200),
]


def generate_random_test_case(length, max_value):
    test_case = [
        [random.randint(0, max_value) for i in range(length)] for j in range(length)
    ]
    return test_case, bruteforce(test_case)


def test_student_algorithm(test_case, answer):
    student = largest_cuboid(test_case)
    if student != answer:
        if len(test_case) < 4:
            response = "Koden feilet for følgende input: (x={:}).".format(
                test_case
            ) + " Din output: {:}. Riktig output: {:}".format(student, answer)
        else:
            response = "Koden feilet på input som er for langt til å vises her"
        print(response)
        sys.exit()


# Tester funksjonen på håndskrevne tester
for test_case, answer in tests:
    test_student_algorithm(test_case, answer)

# Tester funksjonen på tilfeldig genererte tester
for i in range(20):
    test_case, answer = generate_random_test_case(random.randint(1, 3), 10)
    test_student_algorithm(test_case, answer)
for i in range(10):
    test_case, answer = generate_random_test_case(random.randint(1, 20), 100000)
    test_student_algorithm(test_case, answer)
