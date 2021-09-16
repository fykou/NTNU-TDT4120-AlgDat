#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
Vi ønsker å sortere en liste med nn tall, men har veldig liten plass i minnet til datamaskinen vår. 
Vi har kun plass til to av tallene i minnet av gangen, og må ellers ha verdiene lagret på et eksternt medium. 
Maskinen vår har 3 eksterne mediumer (disker) som oppfører seg som stakker. 
Du kan anta at alle disse har plass til alle elementene som skal sorteres, men det er kun plass til nn elementer på dem totalt. 
Du kan også anta at det er nok plass i minnet til alle variabler du trenger for å holde styr på hvor i sorteringen du er.

Skriv en funksjon som sorterer tallene som finnes i den første stakken slik at det minste tallet er på toppen av stakken og det største på bunnen. 
Alle elementene skal ligge i den første stakken etter sortering.

Stakkene her følgende metoder (<variabel-navn>.<metode-navn>):

push(x) - Plasserer xx på toppen stakken.
pop() - Fjerner det øverste elementet i stakken og returnerer dette elementet.
empty() - Returnerer True hvis stakken er tom, ellers False.
peek() - Returnerer det øverste elementet i stakken uten å fjerne dette fra stakken.
'''


def sort(stack1, stack2, stack3):

    while not stack1.empty():
        el1 = stack1.pop()
        
        if stack2.empty():
            stack2.push(el1)
            el1 = stack1.pop()

        while not stack2.empty():
            el2 = stack2.pop()
            if el1 < el2:
                stack3.push(el2)
                if stack2.empty():
                    stack2.push(el1)
                    if stack1.empty:
                        while not stack3.empty():
                            stack2.push(stack3.pop())
                    break
            else:
                stack2.push(el2)
                stack2.push(el1)
                while not stack3.empty():
                    stack2.push(stack3.pop())
                break

    while not stack2.empty():
        stack1.push(stack2.pop())
    



""" class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, operation_counter, element_counter, initial=None):
        self.stack = []
        if initial is not None:
            self.stack = initial

        self.element_counter = element_counter
        self.operation_counter = operation_counter

    def push(self, value):
        if self.element_counter.get_value() <= 0:
            raise RuntimeError(
                "Du kan ikke ta vare på flere elementer på "
                "stakkene enn det fantes originalt."
            )
        self.stack.append(value)
        self.element_counter.decrement()
        self.operation_counter.increment()

    def pop(self):
        if self.element_counter.get_value() >= 2:
            raise RuntimeError(
                "Du kan ikke ha mer enn 2 elementer i minnet " "av gangen."
            )
        self.element_counter.increment()
        self.operation_counter.increment()
        return self.stack.pop()

    def peek(self):
        self.operation_counter.increment()
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


# Tester, høyre side blir toppen av stakken
tests = (
    [4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 2, 1, 7],
    [1, 1, 1, 1],
    [7, 3, 9, 2, 0, 1, 3, 4],
    [7, 3, 0, 13, 48, 49, 233, 9, 2, 0, 1, 3, 4],
    [7, 97, 38, 21, 39, 12, 33, 12, 88, 46, 63, 82, 32, 37, 3, 0, 12, 13, 48]
    + [49, 233, 9, 2, 0, 1, 3, 4],
)

failed = False

for test in tests:
    counter1 = Counter()
    counter2 = Counter()
    stack1 = Stack(counter1, counter2, initial=test[:])
    stack2, stack3 = Stack(counter1, counter2), Stack(counter1, counter2)

    sort(stack1, stack2, stack3)

    result = []
    counter2.value = float("-inf")
    while not stack1.empty():
        result.append(stack1.pop())

    if result != sorted(test):
        print(
            "Feilet for testen {:}, resulterte i listen".format(test)
            + "{:} i stedet for {:}.".format(result, sorted(test))
        )
        failed = True
    else:
        print(
            "Koden brukte {:}".format(counter1.get_value() - len(result))
            + " operasjoner på sortering av {:}".format(test)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.") """