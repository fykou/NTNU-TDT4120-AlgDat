#!/usr/bin/env python
__author__ = "Hoyby"

# incomplete

"""
SMT-solvere brukes ofte til å sjekke at programmer fungerer som de skal, og for å hindre sikkerhetshull. 
SMT-solvere brukes blant annet mye i symbolsk evaluering. 
Et vanlig komponent i en SMT-solver er en teori-solver som har som oppgave å sjekke kandidatløsninger.

Her skal du implementere en forenklet versjon av en teori-solver. Du får en mengde med variabler xi,
en mengde med ligninger xi=xj og en mendge med ulikheter xi>xj eller xi<xj og skal sjekke om det er mulig
å gi tallverdier til alle variablene slik at alle ligningene og alle ulikhetene overholdes.

Mer bestemt skal du implementere check(variables, constraints).
Her er variables en liste med tekststrenger som hver representerer en variabel. 
Parameteren constraints er en liste med tupler på formen (a, comp, b) der a og b er tekststrenger 
fra variables og comp kan være "=", "<" eller ">", som representerer henholdsvis at a=ba=b, a<ba<b eller a>ba>b. 
Funksjonen skal returnere True om det er mulig å gi variablene i variables tallverdier som overholder 
restriksjonene i constraints og False ellers.
"""


class Graph:
    def __init__(self, vertices):
        self.nodes = vertices

    # uses path compression
    def find(self, parent, vertex):
        if parent[vertex] == None:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, root1, root2):
        parent[root1] = root2

    def merge(self, equal, v1, v2):
        if v1 in equal and v2 not in equal:
            equal[v1] = v1, v2
        elif v2 in equal and v1 not in equal:
            equal[v2] = v2, v1
        else:
            equal[v1] = v1, v2

    def KruskalMST(self, E, n):
        parent = dict()
        equal = dict()

        for node in n:
            parent[node] = None

        for edge in E:
            x = edge[0]
            y = edge[1]

            for key in equal:
                for element in equal[key]:
                    if element == x:
                        x = key
                    elif element == y:
                        y = key

            xroot = self.find(parent, x)
            yroot = self.find(parent, y)

            if xroot != yroot:
                if len(edge) == 3:
                    self.merge(equal, x, y)
                else:
                    self.union(parent, x, y)

            elif x == y:
                raise Exception


def check(variables, constraints):
    E = []
    length = len(variables)
    for pred in constraints:
        var1 = pred[0]
        op = pred[1]
        var2 = pred[2]

        if op == "=":
            E.append((var1, var2, "equal"))  # Include equal tag for merge
            length -= 1
        elif op == ">":
            E.append((var1, var2))  # var1 > var2
        elif op == "<":
            E.append((var2, var1))  # var1 < var2

    g = Graph(length)
    print(E)
    try:
        g.KruskalMST(E, variables)
    except Exception:
        print("An exeption occured")
        return False

    return True


tests = [
    # ((["x1"], []), True),
    # ((["x1", "x2"], [("x1", "=", "x2")]), True),
    # ((["x1"], [("x1", ">", "x1")]), False),
    # ((["x1"], [("x1", "=", "x1")]), True),
    # ((["x1", "x2"], [("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x2", "<", "x1"), ("x1", "=", "x2")]), False),
    ((["x1", "x2"], [("x2", ">", "x1"), ("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x1", ">", "x2"), ("x2", ">", "x1")]), False),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x2", "<", "x3"), ("x1", ">", "x3")],
        ),
        False,
    ),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x3", "=", "x1"), ("x2", "<", "x3")],
        ),
        False,
    ),
    ((["x4", "x0", "x1"], [("x1", "<", "x0")]), True),
    ((["x5", "x8"], [("x8", "<", "x5"), ("x8", "<", "x5")]), True),
    ((["x1", "x0", "x2"], []), True),
    (
        (
            ["x4", "x8", "x5"],
            [("x4", "<", "x5"), ("x8", ">", "x5"), ("x5", "<", "x8")],
        ),
        True,
    ),
    (
        (
            ["x5", "x9", "x0"],
            [
                ("x9", ">", "x5"),
                ("x9", "=", "x0"),
                ("x0", "=", "x9"),
                ("x0", "=", "x9"),
            ],
        ),
        True,
    ),
    (
        (
            ["x0", "x6", "x7"],
            [("x7", "=", "x0"), ("x7", ">", "x0"), ("x6", ">", "x0")],
        ),
        False,
    ),
    ((["x8", "x6", "x0"], []), True),
    (
        (
            ["x8", "x7", "x0"],
            [("x8", "=", "x0"), ("x0", "=", "x8"), ("x0", "=", "x8")],
        ),
        True,
    ),
    (
        (
            ["x8", "x4"],
            [
                ("x4", ">", "x8"),
                ("x4", ">", "x8"),
                ("x8", "<", "x4"),
                ("x4", ">", "x8"),
                ("x8", "=", "x4"),
            ],
        ),
        False,
    ),
    ((["x3", "x8", "x5"], [("x3", ">", "x8")]), True),
]


for test_case, answer in tests:
    variables, constraints = test_case
    student = check(variables, constraints)
    if student != answer:
        response = (
            "Koden feilet for følgende input: "
            + "(variables={:}, constraints={:}). ".format(variables, constraints)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        print(response)
        break
