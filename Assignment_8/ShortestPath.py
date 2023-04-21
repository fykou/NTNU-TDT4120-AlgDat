#!/usr/bin/env python
__author__ = "Hoyby"

"""
Som et steg i å forbedre infrastrukturen i et land skal du bygge en vei som knytter samme to fattige landsbyer. 
Mellom landsbyene ligger det et fjellområde hvor byggekostnadene til tider kan være veldig høye. 
Veibyggingsprosjektet har et begrenset budsjett og det er derfor deler av dette området veien ikke kan gå igjennom. 
For å holde kostnaden nede og for å redusere reisetiden ønsker du å finne ut hva den korteste veien du kan bygge er, 
gitt en oversikt over hvor det er for dyrt å bygge.

I denne oppgaven skal du implementere en funksjon shortest_road(build_map, start, end). 
Her er build_map en tabell (en liste av lister) som representerer et rutenett av landskapet. 
For en posisjon (i,j) vil build_map[i][j] være True hvis det er mulig å bygge veien gjennom den gitte ruten og False ellers. 
start og end er tupler på formen (i, j) og angir posisjonen til henholdsvis landsbyen veien skal starte i og landsbyen veien skal slutte i.

En liste av posisjoner danner en gyldig vei hvis den første posisjonen er start, 
den siste posisjonen er end og for en hver posisjon (i,j) i listen har man at build_map[i][j] == True. 
I tillegg må posisjonene være slik at for en hver posisjon (i,j) må den neste posisjonen i listen være
 en av de følgende posisjonene {(i−1,j),(i+1,j),(i,j−1),(i,j+1)}.

Funksjonen shortest_road skal returnere en liste med posisjoner på formen (i, j), der listen danner en gyldig vei, og
det ikke finnes en liste med færre posisjoner som gir en gyldig vei.
Dersom det ikke finnes en slik liste med posisjoner, skal funksjonen din returnere None.
"""


import collections


def shortest_road(build_map, start, end):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for northSouth, eastWest in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= northSouth < len(build_map)
                and 0 <= eastWest < len(build_map[0])
                and build_map[northSouth][eastWest] != False
                and (northSouth, eastWest) not in seen
            ):
                queue.append(path + [(northSouth, eastWest)])
                seen.add((northSouth, eastWest))


def shortest_road_(build_map, start, end):
    path = []
    queue = []
    visited = {}

    queue.append(start)
    visited[start] = True

    while queue:
        s = queue.pop(0)
        print(s)
        path.append(s)
        if s == end:
            return path
        print(build_map)

        north = (s[0] - 1, s[1])
        south = (s[0] + 1, s[1])
        east = (s[0], s[1] + 1)
        west = (s[0], s[1] - 1)

        try:
            if (
                (north not in visited or visited[(north)] != True)
                and build_map[north[0]][north[1]]
                and len(build_map[north[1]]) > north[0]
                and north[0] > -1
                and north[1] > -1
            ):
                queue.append(north)
        except IndexError:
            print("nop")
        try:
            if (
                (south not in visited or visited[(south)] != True)
                and build_map[south[0]][south[1]]
                and len(build_map[south[1]]) > south[0]
                and south[0] > -1
                and south[1] > -1
            ):
                queue.append(south)
        except IndexError:
            print("nop")
        try:
            if (
                (east not in visited or visited[(east)] != True)
                and build_map[east[0]][east[1]]
                and len(build_map[east[0]]) > east[1]
                and east[0] > -1
                and east[1] > -1
            ):
                queue.append(east)
        except IndexError:
            print("nop")
        try:
            if (
                (west not in visited or visited[(west)] != True)
                and build_map[west[0]][west[1]]
                and len(build_map[west[0]]) > west[1]
                and west[0] > -1
                and west[1] > -1
            ):
                queue.append(west)
        except IndexError:
            print("nop")


# Disjoint-set forest
class Set:
    def __init__(self):
        self.__p = self
        self.rank = 0

    @property
    def p(self):
        if self.__p != self:
            self.__p = self.__p.p
        return self.__p

    @p.setter
    def p(self, value):
        self.__p = value.p


def union(x, y):
    x = x.p
    y = y.p
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        y.rank += x.rank == y.rank


# fmt: off
tests = [
    # (([[True, True]], (0, 1), (0, 0)), 2),
    (([[True, False, True]], (0, 0), (0, 2)), None),
    (([[True, True, True]], (0, 0), (0, 2)), 3),
    (([[True, True, False]], (0, 1), (0, 0)), 2),
    (([[True], [True]], (1, 0), (0, 0)), 2),
    (([[True, False], [True, True]], (0, 0), (1, 1)), 3),
    (([[False, True], [True, True]], (0, 1), (1, 0)), 3),
    (([[True, True], [True, True]], (1, 1), (0, 0)), 3),
    (([[False, False, True], [True, False, True]], (1, 2), (0, 2)), 2),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, False], [True, False]], (0, 0), (1, 0)), 2),
    (([[True, False], [False, False], [True, True]], (0, 0), (2, 1)), None),
    (([[False, False, True], [False, False, True], [True, False, True]], (0, 2), (2, 2)), 3),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, True, True], [False, False, False]], (0, 2), (0, 1)), 2),
    (([[True, False, True], [True, False, False]], (0, 2), (1, 0)), None),
    (([[True, True], [False, False], [False, True]], (0, 0), (0, 1)), 2),
    (([[False, True, False], [False, True, False]], (1, 1), (0, 1)), 2),
]
# fmt: on

for test_case, answer in tests:
    build_map, start, end = test_case
    student_map = [i[:] for i in build_map]
    student = shortest_road(student_map, start, end)
    response = None
    if answer is None and student is not None:
        response = "Du returnerte en liste med posisjoner når riktig svar var None."
    elif student is None and answer is not None:
        response = "Du returnerte None, selv om det finnes en løsning."
    elif student is not None and answer < len(student):
        response = "Det finnes en liste med færre koordinater som fortsatt danner en gyldig vei."
    elif student is not None:
        for pos in student:
            if not (0 <= pos[0] < len(build_map) and 0 <= pos[1] < len(build_map[0])):
                response = "Du prøver å bygge utenfor kartet."
                break
            if not build_map[pos[0]][pos[1]]:
                response = "Du prøver å bygge en plass der det ikke er mulig å bygge."
                break
        else:
            disjoint_set = {pos: Set() for pos in student}
            for pos in student:
                for i, j in [
                    (pos[0] + 1, pos[1]),
                    (pos[0] - 1, pos[1]),
                    (pos[0], pos[1] + 1),
                    (pos[0], pos[1] - 1),
                ]:
                    if (i, j) in disjoint_set and disjoint_set[
                        (i, j)
                    ].p != disjoint_set[pos].p:
                        union(disjoint_set[pos], disjoint_set[(i, j)])
            if start not in disjoint_set:
                response = "Du har ikke med startlandsbyen i listen."
            if end not in disjoint_set:
                response = "Du har ikke med sluttlandsbyen i listen."
            if disjoint_set[start].p != disjoint_set[end].p:
                response = "Listen din gir ikke en sammenhengende vei."
    if response is not None:
        response += " Input: (build_map={:}, start={:}, ".format(build_map, start)
        response += "end={:}). Ditt svar: {:}".format(end, student)
        print(response)
        break
