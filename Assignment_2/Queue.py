#!/usr/bin/env python
__author__ = "Hoyby"

"""
For at studentassistentene skal kunne hjelpe studentene i riktig og rettferdig rekkefølge, 
trenger man et system som holder styr på hvem som venter på hjelp og hvilken rekkefølge disse skal få hjelp i. 
En kø (FIFO) passer godt til dette. Implementer en slik kø ved å fylle ut koden for Queue klassen under.

Funksjonene enqueue og dequeue skal fungere på samme måte som henholdsvis ENQUEUEENQUEUE og DEQUEUEDEQUEUE operasjonene presentert i boken.
I __init__ metoden kan du initialisere de interne verdiene du trenger. 
max_size argumentet til __init__ metoden sier hvor mange elementer det maksimalt kommer til å være i køen på et vilkårlig tidspunkt.

Merk: Det er ikke lov til å bruke queue biblioteket, collections.deque eller andre innebygde implementasjoner av køer.
"""


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self._queue = []

    def enqueue(self, value):
        if self.size >= self.max_size:
            self._queue.append(value)
            self.size += 1
        else:
            self._queue.append(value)
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("No elements")
        else:
            first = self._queue[0]
            del self._queue[0]
            return first


# -------------------- Test --------------------

# import unittest

# q = Queue(3)


# class Test(unittest.TestCase):
#    def test_a(self):
#        self.assertEqual(q._queue, [])
#        q.enqueue(10)
#        self.assertEqual(q._queue, [10])
#        q.enqueue(15)
#        self.assertEqual(q._queue, [10, 15])

#    def test_b(self):
#        self.assertEqual(q._queue, [10, 15])
#        q.dequeue()
#        self.assertEqual(q._queue, [15])
#        q.dequeue()
#        self.assertEqual(q._queue, [])


# unittest.main()


def tester(values, sequence, max_size):
    """
    Tester en oppgitt sekvens av operasjoner og sjekker at verdiene
    (values) kommer ut i riktig rekkefølge.
    """
    index = 0
    queue = Queue(max_size)
    output = []
    for action in sequence:
        if action == "enqueue":
            queue.enqueue(values[index])
            index += 1
        elif action == "dequeue":
            output.append(queue.dequeue())

    if output != values:
        print(
            "Feilet for følgende sekvens av operasjoner "
            + "'{:}' med verdiene ".format(", ".join(sequence))
            + "'{:}' og maksimal størrelse".format(", ".join(map(str, values)))
            + "'{:}'".format(max_size)
        )
        return True
    return False


tests = (
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        3,
    ),
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        1,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "dequeue",
            "dequeue",
        ),
        4,
    ),
)

failed = False

for values, sequence, max_size in tests:
    failed |= tester(values, sequence, max_size)

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
