#!/usr/bin/env python
__author__ = "Alex Høyby"

#incomplete

'''
Ofte trenger man å kunne skalere bilder slik at de får plass på mindre skjermer. 
I denne oppgaven skal du implementere en metode for akkurat dette. 
Denne metoden kalles sømfjerning (seam carving) og går ut på å fjerne stier av piksler slik at minst mulig informasjon forsvinner fra bildet. 
Eksempler på dette kan ses i denne Wikipedia-artikkelen og i denne YouTube-videoen. 
Metoden kan anvendes både til å redusere høyden og bredden på et bilde, men vi skal kun bry oss om bredden i denne oppgaven.

Sømfjerning fungerer på følgende måte:

Finn vekter som angir hvor viktig hver piksel i bildet er.
Finn en sti av piksler fra topp til bunn med lavest mulig vektsum.
Fjern alle piksler i denne stien fra bildet.
En sti kan bevege seg på skrå, men kan ikke hoppe mer enn én piksel bortover per rad.

Koden din skal kun utføre steg 2. 
Det vil si at den tar inn en todimensjonal liste (se nedenfor) av vekter og skal gi ut en liste av pikslene som ligger på denne minimale stien. 
En måte å gjøre dette på er å finne den minimale kostnaden for en stier frem til hver piksel. 
Dette kan man regne ut rad for rad. I etterkant kan man så finne den pikselen på den nederste raden som har lavest kostand og velge stien denne representerer. 
Et eksempel på dette er vist i figuren under, hvor man iterativt regner ut disse kostnadene. 
I bildet viser pilene den forrige pikselen langs stien med lavest kostnad frem til den gitte pikselen.


Implementer funksjonen find_path(weights) som tar inn en todimensjonal liste av vekter på formatet [rad_1, rad_2, ..., rad_n] 
hvor rad_i er en liste av vektene i rad ii. Funksjonen skal returnere en liste av pikslene i stien med lavest samlet vekt. 
Hver piksel skal representeres ved som et tuppel (x, y), der x er kolonnen pikselen ligger i og y er raden pikselen ligger på, 
begge 0-indeksert. For eksemplet i figuren over, så skulle funksjonen ha returnert [(0, 0), (1, 1), (0, 2), (0, 3)]. 
Finnes det flere stier som har samme minste vekt, kan du velge hvilken du vil returnere.
'''


def find_path(weights):
    # Skriv koden din her
    pass


# Tester på formatet (vekter, minste mulige vekt på sti).
tests = [
    ([[1]], 1),
    ([[1, 1]], 1),
    ([[1], [1]], 2),
    ([[2, 1], [2, 1]], 2),
    ([[1, 1], [1, 1]], 2),
    ([[2, 1], [1, 2]], 2),
    ([[3, 2, 1], [1, 3, 2], [2, 1, 3]], 4),
    ([[1, 10, 3, 3], [1, 10, 3, 3], [10, 10, 3, 3]], 9),
    ([[1, 2, 7, 4], [9, 3, 2, 5], [5, 7, 8, 3], [1, 3, 4, 6]], 10),
]


# Verifiserer at en løsning er riktig gitt vektene, stien og den minst
# mulige vekten man kan ha på en sti.
def verify(weights, path, optimal):
    if len(path) != len(weights):
        return False, "Stien er enten for lang eller for kort."

    last = -1
    for index, element in enumerate(path):
        if type(element) != tuple:
            return False, "Stien består ikke av tupler."
        if len(element) != 2:
            return False, "Stien består ikke av tupler på formatet (x,y)."
        if index != element[1]:
            return False, "Stien er ikke vertikal."
        if element[0] < 0 or element[0] >= len(weights[0]):
            return False, "Stien går utenfor bildet."
        if last != -1 and not last - 1 <= element[0] <= last + 1:
            return False, "Stien hopper mer enn en piksel per rad."
        last = element[0]

    weight = sum(weights[y][x] for x, y in path)
    if weight != optimal:
        return (
            False,
            "Stien er ikke optimal. En optimal sti ville hatt"
            + "vekten {:}, mens din hadde vekten {:}".format(optimal, weight),
        )

    return True, ""


failed = False

for test, optimal_weight in tests:
    answer = find_path([row[:] for row in test])
    correct, error_message = verify(test, answer, optimal_weight)
    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")