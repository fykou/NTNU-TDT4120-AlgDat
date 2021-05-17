#!/usr/bin/env python
__author__ = "Alex Høyby"

#incomplete

'''
Et beslutningstre er et binært tre hvor alle løvnodene er beslutninger og alle de interne nodene representerer ja-/nei-spørsmål. 
Treet er slikt at man kan ta en situasjon, gjenstand eller lignende og traverse treet fra rotnoden til en løvnode
 ved å i hver interne node gå til det venstre barnet hvis svaret på spørsmålet er ja, og til det høyre barnet hvis svaret er nei. 
 Den løvnoden man kommer til vil tilsvare den beslutningen man skal ta i situasjonen, en klassifikasjon av gjenstanden eller lignende.

Beslutningstrær som minimaliserer antall spørsmål som må stilles (i forventning, gitt en fordeling over
 sannsynlighet til hver beslutning) har mange forskjellige anvendelser. Et eksempel på en slik anvendelse kan være telefonsupport, 
 hvor man ønsker å minimere tiden man trenger å bruke på å identifisere problemet til brukeren. Dette er spesielt viktig hos nødsentraler, 
 hvor det er viktig å få hjulpet innringeren raskest mulig.

I denne oppgaven skal vi implementer en funksjon som bygger et optimalt beslutningstre, 
hvor vi antar at etter vi har bygget treet vil en ekspert konstruere ja-/nei- spørsmålene basert på hvordan treet er bygget opp. 
Vi trenger altså kun å konstruere et tre som skiller mellom alternativene og resulterer i det minste antallet forventet spørsmål. 
Funksjonen build_decision_tree(decisions) tar inn en liste av beslutninger, decisions, 
som er en liste av tuppler på formen (name, probability). Funksjonen skal returnere en oppslagstabell (dictionary)
 hvor hver nøkkel skal være navnet til en beslutning og verdien skal være en streng av enere og nuller som representerer
  hvilke spørsmål man må svare ja og nei på for å komme frem til den gitte beslutningen. Altså, hvis man for å komme
   frem til en gitt beslutning må svare «ja, nei, ja», så ender man opp med strengen «010».

Som et eksempel sett decisions = [("a", 0.5), ("b", 0.25), ("c", 0.25)]

Da vil et mulig optimalt beslutningstre se ut som dette


For dette beslutningstreet skal build_decision_tree(decisions) returnere oppslagstabellen {"a": "0", "b": "10", "c": "11"}.

I situasjoner hvor det finnes mange forskjellige optimale beslutningstrær vil alle optimale beslutningstrær være gyldige svar.
'''


from heapq import heappush, heappop


def build_decision_tree(decisions):
    # Skriv koden din her
    pass


tests = [
    ([("a", 0.5), ("b", 0.5)], 1),
    ([("a", 0.99), ("b", 0.01)], 1),
    ([("a", 0.5), ("b", 0.25), ("c", 0.25)], 1.5),
    ([("a", 0.33), ("b", 0.33), ("c", 0.34)], 1.66),
    ([("a", 0.25), ("b", 0.25), ("c", 0.25), ("d", 0.25)], 2),
    ([("a", 0.4), ("b", 0.2), ("c", 0.2), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.25), ("c", 0.25), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.2), ("c", 0.2), ("d", 0.2), ("e", 0.1)], 2.3),
]


def check_overlap_and_add_to_tree(tree, value):
    is_valid = len(tree) == 0
    for v in value:
        if v in tree:
            tree = tree[v]
        else:
            if len(tree) == 0 and not is_valid:
                return False
            tree[v] = {}
            tree = tree[v]
            is_valid = True

    return is_valid


def test_answer(student, test_case, correct_answer):
    if len(test_case) <= 20:
        feedback = "Feilet for tilfellet {:}.".format(
            test_case
        ) + " Ditt svar var {:}.\n".format(student)
    else:
        feedback = "Koden returnerte et galt svar:\n"

    if not isinstance(student, dict):
        feedback += "Funksjonen skal returnere en oppslagstabell (dictionary)."
        print(feedback)
        return False

    tree = {}
    expectance = 0
    for value, prob in test_case:
        if value not in student:
            feedback += "Beslutningen {:} er ikke med i treet.".format(value)
            print(feedback)
            return False

        encoding = student[value]
        if not isinstance(encoding, str) or not set(encoding) <= {"1", "0"}:
            feedback += (
                "Hver beslutning skal ha en streng av nuller og "
                + "enere knyttet til seg. "
            )
            print(feedback)
            return False

        if not check_overlap_and_add_to_tree(tree, encoding):
            feedback += "En av beslutningene er en internnode."
            print(feedback)
            return False

        expectance += prob * len(encoding)

    if expectance > correct_answer + 0.0000001:
        feedback += (
            "Beslutningstreet ditt er ikke optimalt. Det skulle "
            + "hatt en forventning på {:}".format(correct_answer)
            + " spørsmål, men har en forventning på "
            + str(expectance)
        )
        print(feedback)
        return False

    return True


passed = True
for test_case, answer in tests:
    student = build_decision_tree(test_case)
    passed &= test_answer(student, test_case, answer)

if passed:
    print("Passerte alle testene")