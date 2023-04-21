#!/usr/bin/env python
__author__ = "Hoyby"

"""
En fabrikk kjøper inn store flate metallstykker og ønsker å dele disse opp slik at de kan maksimere profitten sin når de selger metallstykkene videre. 
De skal dele metallstykkene i mindre rektangulære stykker hvor sidekantene har heltallslengder.

Implementer funksjonen sheet_cutting(w, h, p) som skal returnere den beste prisen man kan få ved deling av et metallstykke med bredde w og høyde h, 
gitt prisene i p. Her er p en oppslagstabell (dictionary) hvor nøklene er tupler på formen (x, y) og verdien til
en gitt nøkkel er prisen på et metallstykke med bredde x og høyde y.
"""


def sheet_cutting(w, h, p, val=None):
    if val is None:
        val = {}

    if w < 1 or h < 1:
        return 0

    # check for already existing solutions
    if (w, h) in val:
        return val[w, h]
    elif (h, w) in val:
        return val[h, w]

    val[w, h] = p[w, h]
    for i in range(1, w):
        val[w, h] = max(
            val[w, h], sheet_cutting(w - i, h, p, val) + sheet_cutting(i, h, p, val)
        )

    for i in range(1, h):
        val[w, h] = max(
            val[w, h], sheet_cutting(w, h - i, p, val) + sheet_cutting(w, i, p, val)
        )

    return val[w, h]


tests = [
    ({(1, 1): 1}, 1, 1, 1),
    ({(1, 1): 1, (2, 1): 3, (1, 2): 3, (2, 2): 3}, 2, 2, 6),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 5}, 2, 2, 5),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 0, (1, 2): 0, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (1, 2): 1}, 1, 2, 2),
    ({(1, 1): 1, (2, 1): 3}, 2, 1, 3),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (3, 1): 4, (2, 2): 3, (3, 2): 7},
        3,
        2,
        8,
    ),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (1, 3): 4, (2, 2): 3, (2, 3): 7},
        2,
        3,
        8,
    ),
    (
        {(1, 1): 1, (2, 1): 3, (3, 1): 3, (4, 1): 7, (5, 1): 3, (6, 1): 8},
        6,
        1,
        10,
    ),
    (
        {
            (1, 1): 1,
            (1, 2): 2,
            (2, 1): 2,
            (1, 3): 1,
            (3, 1): 1,
            (1, 4): 2,
            (4, 1): 2,
            (1, 5): 2,
            (5, 1): 2,
            (1, 6): 5,
            (6, 1): 5,
            (1, 7): 10,
            (7, 1): 10,
            (1, 8): 10,
            (8, 1): 10,
            (2, 2): 5,
            (2, 3): 5,
            (3, 2): 5,
            (2, 4): 2,
            (4, 2): 2,
            (2, 5): 10,
            (5, 2): 10,
            (2, 6): 7,
            (6, 2): 7,
            (2, 7): 11,
            (7, 2): 11,
            (2, 8): 16,
            (8, 2): 16,
            (3, 3): 1,
            (3, 4): 1,
            (4, 3): 1,
            (3, 5): 1,
            (5, 3): 1,
            (3, 6): 11,
            (6, 3): 11,
            (3, 7): 11,
            (7, 3): 11,
            (3, 8): 24,
            (8, 3): 24,
            (4, 4): 12,
            (4, 5): 25,
            (5, 4): 25,
            (4, 6): 29,
            (6, 4): 29,
            (4, 7): 25,
            (7, 4): 25,
            (4, 8): 9,
            (8, 4): 9,
            (5, 5): 12,
            (5, 6): 10,
            (6, 5): 10,
            (5, 7): 26,
            (7, 5): 26,
            (5, 8): 45,
            (8, 5): 45,
            (6, 6): 35,
            (6, 7): 44,
            (7, 6): 44,
            (6, 8): 50,
            (8, 6): 50,
            (7, 7): 1,
            (7, 8): 41,
            (8, 7): 41,
            (8, 8): 5,
        },
        8,
        8,
        91,
    ),
]

failed = False

for prices, width, height, solution in tests:
    student_answer = sheet_cutting(width, height, prices)
    if student_answer != solution:
        failed = True
        print(
            "Feilet for testen w={:} h={:} ".format(width, height)
            + "p={:}, resulterte i ".format(prices)
            + "svaret {:} i stedet for {:}.".format(student_answer, solution)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
