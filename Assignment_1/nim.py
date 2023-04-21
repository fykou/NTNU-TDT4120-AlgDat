#!/usr/bin/env python
__author__ = "Hoyby"

"""
Implementer en funksjon, take_pieces, som tar inn antall gjenværende fyrstikker. 
Funksjonen skal returnere det antallet fyrstikker du må ta for å garantere at du vinner. 
Hvis det ikke er mulig å garantere at du vinner, så kan du returnere et hvilket som helst, gyldig antall fyrstikker.
"""


def take_pieces(n):
    maxDraw = 7
    if (n - 1) % (maxDraw + 1) == 0 or n == 1:
        return 1  # You lost
    else:
        return (n - 1) % (maxDraw + 1)


if __name__ == "__main__":
    tests = [
        (1, None),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 6),
        (8, 7),
    ]

    for test, correct_answer in tests:
        answer = take_pieces(test)

        if answer not in (1, 2, 3, 4, 5, 6, 7):
            print("Funksjonen returnerte en ugyldig verdi: {:}".format(answer))

        if answer != correct_answer and correct_answer is not None:
            print("Koden feilet for følgende antall fyrstikker: {:}".format(test))
