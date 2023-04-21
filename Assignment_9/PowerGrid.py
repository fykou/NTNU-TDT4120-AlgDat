#!/usr/bin/env python
__author__ = "Hoyby"

#incomplete

'''
I en sentrum av en storby er det behov for å bygge ut strømnettet. 
Det er overføringskapasiteten fra kraftnettet til nettstasjonene (såkalte trafokiosker) som skal utbedres.

Storbyen er formet som et regulert rutenett med m×nm×n veier. 
Veiene som går horisontalt er nummerert fra 00 til m−1m−1 og veiene som går vertikalt er nummerert fra 0 til n−1. 
En posisjon i veinettet er gitt av (i,j) som representerer krysset mellom vei i som går horisontalt og vei j som går vertikalt. 
Et eksempel er vist på figuren nedenfor med m=4 og n=3:


Her er hver kant en vei og posisjonen (2,1) er merket med en rød sirkel.

Du skal implementere funksjonen power_grid(m, n, substations). Her er m og n som forklart over. 
Posisjonene til nettstasjonene er gitt av tupler på formen (i, j) som sier at det er en nettstasjon i 
krysset gitt av posisjonen (i,j). Alle nettstasjonene ligger i ulike kryss.

Det skal legges kraftledninger i bakken. Alle kraftledningene må gå langs veiene, 
siden man ellers må grave opp en bygning, noe som naturligvis er for dyrt. 
Disse nye kraftledingene skal koble sammen alle nettstasjonene (potensielt via andre nettstasjoner). 
Det er ønskelig å gjøre dette så billig så mulig ved å gjøre totallengden av ledningene så liten som mulig, 
målt i antall veistrekninger. En veistrekning her går fra et kryss til neste kryss 
(altså fra posisjon (i,j) til (i+1,j), (i−1,j), (i,j+1) eller (i,j−1)).

En nettstasjon kan være koblet til flere kraftledninger og en veistrekning kan ha flere kraftledninger, 
men en kraftledning kan ikke forgrene seg.

Funksjonen skal returnere totallengden av kraftledningene som må legges, der lengden måles i antall veistrekninger.

Funksjonen bør ha kjøretid på O(mnlg(mn)).
'''


def power_grid(m, n, substations):
    # Skriv din kode her
    

tests = [
    ((2, 2, [(1, 1)]), 0),
    ((2, 2, [(0, 0), (1, 1)]), 2),
    ((2, 2, [(0, 0), (0, 1), (1, 0)]), 2),
    ((2, 2, [(0, 0), (0, 1), (1, 0), (1, 1)]), 3),
    ((3, 3, [(0, 2), (2, 0)]), 4),
    ((3, 3, [(0, 0), (1, 1), (2, 2)]), 4),
    ((3, 3, [(1, 1), (0, 1), (2, 1)]), 2),
    ((3, 3, [(1, 2)]), 0),
    ((3, 3, [(2, 0), (1, 1), (0, 1)]), 3),
    ((2, 3, [(1, 1)]), 0),
    ((2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]), 3),
    ((2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]), 3),
    ((3, 3, [(0, 1), (0, 2), (2, 1), (2, 2)]), 4),
    ((3, 3, [(0, 1), (0, 2), (1, 2), (2, 1)]), 4),
    ((2, 3, [(1, 0), (1, 1), (0, 2)]), 3),
    ((2, 3, [(1, 0)]), 0),
    ((3, 2, [(1, 0), (2, 1), (0, 0)]), 3),
    ((3, 3, [(0, 1), (1, 1), (2, 1), (0, 0)]), 3),
    ((3, 3, [(0, 2)]), 0),
]

for test_case, answer in tests:
    m, n, substations = test_case
    student = power_grid(m, n, substations)
    if student != answer:
        response = (
            "Koden feilet for følgende input: "
            + "(m={:}, n={:}, substations={:}). ".format(m, n, substations)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        print(response)
        break
