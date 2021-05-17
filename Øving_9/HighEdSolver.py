#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
Høyere utdanning har i Norge vært preget av flere fusjoner de siste årene. Dette kan fort bli problematisk å holde orden på, 
så derfor trenger vi din hjelp.

Du skal fullføre klassen HigherEdSolver. 
Funksjonen initialize(institutions) får inn som argument en liste med tekststrenger som hver representerer en institusjon innen høyere utdanning. 
Du må bruke denne listen til å initialisere en datastruktur som kan brukes av de to andre funksjonene. 
Funksjonen fuse(institution1, institution2, new_institution) slår sammen to utdanningsinstitusjoner. 
Her skal institution1 slås sammen med institution2, begge representert med tekststrenger. 
De legges under en ny institusjon representert ved tekststrengen new_institution. 
Alle institusjonene som eventuelt lå under institution1 og institution2 vil nå også ligge under new_institution. 
Hverken institution1 og institution2 vil ligge under en annen institusjon når funksjonen blir kalt. 
Den siste funksjonen er parent_institution(institution). 
Her er institution en tekststreng som representerer en utdanningsinstitusjon som potensielt ligger under en annen institusjon. 
Funksjonen skal returnere tekststrengen som representerer utdanningsinstitusjonen som institution ligger under, 
som er institusjonen selv om den ikke ligger under en annen institusjon.

I hver test instansieres et HigherEdSolver-objekt. Deretter vil funksjonen initialize(institution) vil kun bli kalt én gang, 
før noen av de andre funksjonskallene. Så vil det være en rekke med kall
til fuse(institution1, institution2, new_institution) og parent_institution(institution). 
Du får godkjent dersom parent_institution(institution) returnerer riktig institusjon hver gang.

Et eksempel:

initialize(["UniA", UniB", UniC"])
parent_institution("UniB") skal returnere "UniB" siden institusjonen ikke ligger under en annen institusjon.
fuse("UniA", UniB", UniAogB")
parent_institution("UniA") skal returnere "UniAogB" siden det er det institusjonen ligger under etter sammenslåingen.
parent_institution("UniAogB") skal returnere "UniAogB" siden denne institusjonen ikke ligger under en annen institusjon.
fuse("UniAogB", "UniC", "UniABC")
parent_institution("UniB") skal returnere "UniABC" siden det er det institusjonen ligger under etter sammenslåingene.
'''


class HigherEdSolver:
    def initialize(self, institutions):
        self.dict = {inst: inst for inst in institutions}


    def parent_institution(self, institution):
        if self.dict[institution] != institution:
            self.dict[institution] = self.parent_institution(self.dict[institution])
        return self.dict[institution]

    def fuse(self, institution1, institution2, new_institution):
        root1 = self.parent_institution(institution1)
        root2 = self.parent_institution(institution2)
        self.dict[root1] = new_institution
        self.dict[root2] = new_institution
        self.dict[new_institution] = new_institution


class HigherEdTestCase:
    def __init__(self, calls, print_case):
        self.calls = calls
        self.print_case = print_case

    def test(self, initialize, parent_institution, fuse):
        for index, call in enumerate(self.calls):
            if call[0] == "initialize":
                initialize(call[1])
            elif call[0] == "parent_institution":
                res = parent_institution(call[1])
                assert res == call[2], (
                    "Kall:\n"
                    + self.calls_to_str(index + 1)
                    + '\nSistnevte returnerte "{:}", men skulle '.format(res)
                    + 'returnere "{:}"'.format(call[2])
                    if self.print_case
                    else "parent_institution returnerte feil"
                )
            elif call[0] == "fuse":
                fuse(call[1], call[2], call[3])

    def calls_to_str(self, index=None):
        s = ""
        for call in self.calls[:index]:
            if call[0] == "initialize":
                s += 'initialize(["' + '", "'.join(call[1]) + '"])'
            elif call[0] == "parent_institution":
                s += 'parent_institution("{:}")'.format(call[1])
            elif call[0] == "fuse":
                s += 'fuse("{:}", "{:}", "{:}")'.format(call[1], call[2], call[3])
            s += "\n"
        return s


tests = [
    [
        ("initialize", ["UniK", "UniR", "UniW"]),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniR", "UniR"),
        ("fuse", "UniK", "UniW", "UniC"),
    ],
    [
        ("initialize", ["UniP", "UniB", "UniY", "UniJ", "UniK"]),
        ("fuse", "UniK", "UniB", "UniT"),
        ("fuse", "UniY", "UniT", "UniM"),
        ("fuse", "UniP", "UniM", "UniV"),
        ("parent_institution", "UniK", "UniV"),
    ],
    [
        ("initialize", ["UniL", "UniQ", "UniB", "UniY", "UniU"]),
        ("parent_institution", "UniL", "UniL"),
        ("fuse", "UniY", "UniB", "UniF"),
        ("parent_institution", "UniB", "UniF"),
        ("fuse", "UniQ", "UniF", "UniX"),
        ("parent_institution", "UniY", "UniX"),
    ],
    [
        ("initialize", ["UniG", "UniS", "UniC", "UniU"]),
        ("parent_institution", "UniG", "UniG"),
        ("fuse", "UniS", "UniC", "UniM"),
    ],
    [
        ("initialize", ["UniB", "UniA", "UniE", "UniO", "UniG"]),
        ("parent_institution", "UniE", "UniE"),
        ("fuse", "UniO", "UniA", "UniN"),
        ("fuse", "UniG", "UniE", "UniD"),
        ("fuse", "UniN", "UniD", "UniW"),
        ("parent_institution", "UniB", "UniB"),
    ],
    [
        ("initialize", ["UniZ", "UniR", "UniM", "UniC", "UniW"]),
        ("fuse", "UniC", "UniM", "UniK"),
        ("parent_institution", "UniC", "UniK"),
    ],
    [
        ("initialize", ["UniE", "UniR", "UniK", "UniQ", "UniD"]),
        ("fuse", "UniD", "UniK", "UniN"),
        ("parent_institution", "UniR", "UniR"),
        ("parent_institution", "UniE", "UniE"),
        ("parent_institution", "UniQ", "UniQ"),
    ],
    [
        ("initialize", ["UniN", "UniZ", "UniY", "UniA", "UniF"]),
        ("fuse", "UniZ", "UniF", "UniK"),
        ("fuse", "UniN", "UniK", "UniX"),
        ("parent_institution", "UniZ", "UniX"),
        ("fuse", "UniA", "UniY", "UniC"),
    ],
    [
        ("initialize", ["UniG", "UniK", "UniI", "UniM"]),
        ("parent_institution", "UniG", "UniG"),
        ("fuse", "UniM", "UniI", "UniY"),
        ("fuse", "UniY", "UniG", "UniS"),
    ],
    [
        ("initialize", ["UniT", "UniK", "UniC"]),
        ("parent_institution", "UniC", "UniC"),
        ("fuse", "UniK", "UniC", "UniZ"),
    ],
    [
        ("initialize", ["UniX", "UniM", "UniY", "UniA", "UniI"]),
        ("fuse", "UniA", "UniI", "UniK"),
        ("parent_institution", "UniM", "UniM"),
        ("fuse", "UniM", "UniY", "UniU"),
        ("parent_institution", "UniI", "UniK"),
        ("fuse", "UniU", "UniK", "UniW"),
    ],
    [
        ("initialize", ["UniK", "UniZ", "UniY"]),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniK", "UniK"),
        ("fuse", "UniY", "UniZ", "UniQ"),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniY", "UniQ"),
    ],
    [
        ("initialize", ["UniC", "UniJ", "UniD", "UniI", "UniQ"]),
        ("fuse", "UniQ", "UniI", "UniB"),
        ("fuse", "UniC", "UniJ", "UniS"),
        ("parent_institution", "UniD", "UniD"),
        ("parent_institution", "UniI", "UniB"),
    ],
    [
        ("initialize", ["UniU", "UniO", "UniI", "UniS"]),
        ("fuse", "UniO", "UniS", "UniW"),
        ("parent_institution", "UniI", "UniI"),
        ("parent_institution", "UniU", "UniU"),
    ],
]


for test_case in tests:
    test_case = HigherEdTestCase(test_case, True)
    higher_ed_solver = HigherEdSolver()
    try:
        test_case.test(
            higher_ed_solver.initialize,
            higher_ed_solver.parent_institution,
            higher_ed_solver.fuse,
        )
    except AssertionError as e:
        print(str(e))
        break