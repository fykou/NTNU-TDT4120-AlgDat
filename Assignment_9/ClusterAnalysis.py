#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
En mulig anvendelse av minimale spenntrær er klyngeanalyse (engelsk clustering). 
I klyngeanalyse ønsker vi å gruppere elementene i kk ulike klynger, 
slik at elementene innad i en klynge er likere hverandre enn elementer utenfor klyngen. 
Dette kan vi oppnå ved å lage et minimalt spenntre (f.eks. med Kruskals algoritme) basert på en avstandsfunksjon, 
men stoppe når vi har kk trær (og ikke legge til de siste k−1k−1 kantene som trengs for et minimalt spenntre). 
Alternativt kan vi lage et minimalt spenntre og fjerne de k−1k−1 tyngste kantene. 
Ved å bruke minimale spenntrær kan vi garantere at vi maksimerer den minste avstanden mellom elementer i forskjellige klynger. 
Vi maksimerer altså seperasjonsavstanden til klyngene. Figuren under viser et eksempel på gruppering av fem elementer i to klynger.


I denne oppgaven ønsker vi å utføre klyngeanalyse på dyr basert på gensekvensen deres. 
Som avstandsfunksjon skal vi anvende Hamming-avstanden mellom gensekvensen til dyrene. 
Hamming-avstanden til to strenger av lik lengde er definert som antall posisjoner det står ulike
symboler (bokstaver) på i de to strengene. F.eks. vil strengene "AAB" og "ABB" ha en Hamming-avstand på 1,
siden det er kun den andre bokstaven som er forskjellig i strengene. Strengene "BAB" og "ABA" har derimot en Hamming-avstand på 3,
siden det ikke står like symboler på noen av posisjonene i strengene.

Du skal i denne oppgaven fullføre implementasjonen av find_animal_groups(animals, k) funksjonen.
Her er animals en liste av dyr og består av tupler på formen (navn, gensekvens). k er antall klynger som ønskes. 
Funksjonen skal returnere en liste bestående av kk lister, hvor de kk listene representerer hver sin
klynge og skal bestå av navnene til dyrene som finnes i denne klyngen. Klyngene må være slik at seperasjonsavstanden,
basert på Hamming-avstanden til gensekvensen til dyrene, er størst mulig. Er det flere mulige inndelinger i klynger
som maksimerer seperasjonsavstanden kan du returnere hvilken som helst av disse.

I koden under er find_animal_groups delvis implementert og du kan selv velge om du vil fortsette
på denne implementasjonen eller om du vil lage din egen. Implementasjonen av find_animal_groups gjør følgende:

Lager en liste av Hamming-avstand mellom hvert par av dyr på formen (i, j, avstand),
hvor i og j indikerer at dette er avstanden mellom dyr i og j.
Lager klynger basert på listen produsert i steg 1.
Gjør om klyngene produsert i steg 2 til å bruke navn og ikke indekser.
For steg 1 mangler implementasjonen av Hamming-avstanden, i funksjonen hamming_distance.
I steg 2 mangler koden for å finne disse klyngene. Denne kan implementeres i funksjonen find_clusters, 
som tar inn listen fra 1, samt antall dyr, nn, og antall klynger, k. 
find_clusters skal returnere en liste av :katex: lister, hvor hver indre liste representerer en klynge og består av indeksene til dyrene i klyngen.

Eksempel: La dyrene vi skal grupper være Ugle, Mus, Rotte og la disse ha gensekvenser AGAG, CTTC, CGTC. Vi ønsker å lage to klynger.
I steg 1 skal vi da produsere listen [(0, 1, 4), (0, 2, 3), (1, 2, 1)], siden Hamming-avstanden til AGAG og CTTC er 44,
mens den for AGAG og CGTC er 33 og for CTTC og CGTC er den 11. I steg 2 får vi inn denne listen som E,
samt verdiene n = 3, k = 2. Siden Hamming-avstanden mellom mus og rotter er mindre enn for noen av de andre parene,
havner disse i samme klynge, og steg 2 returnerer listen [[0], [1, 2]]. Dette siden vi skal ha to klynger.
I steg 3 gjøres denne listen om til [["Ugle"], ["Mus", "Rotte"]].
'''


def merge(l): 
    out = []
    while len(l)>0:
        first, *rest = l
        first = set(first)
        lf = -1
        while len(first)>lf:
            lf = len(first)
            rest2 = []
            for r in rest:
                if len(first.intersection(set(r)))>0:
                    first |= set(r)
                else:
                    rest2.append(r)     
            rest = rest2
        out.append(first)
        l = rest
    return out


def union(parent, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)
    if root1 != root2:
        parent[root2] = root1


def find(parent, vertex):
    if parent[vertex] == None:
        return vertex
    return find(parent, parent[vertex])


def hamming_distance(s1, s2):
    count = 0
    for i in range(0, min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
    return count


def find_clusters(E, n, k):
    if k > n:
        return print("Error")
    MSP = []
    parent = dict()
    for i in range(0, n):
        parent[i] = None
    edges_sorted = sorted(E, key=lambda cost: cost[2], reverse=True)
    for edge in edges_sorted:
        if find(parent, edge[0]) != find(parent, edge[1]): # Checks if edges has same root (to prevent a cycle)
            if list(parent.values()).count(None) == k: # Checks the number of root nodes against k
                for key in parent:
                    if parent[key] == None:
                        if not any(key in i for i in MSP): # Checks wether one or both of the root nodes are missing
                            MSP.append([key])
                break
            union(parent, edge[0], edge[1])
            MSP.append([edge[0], edge[1]]) # TODO: put edges in same list
    return merge(MSP)



def find_animal_groups(animals, k):
    # Lager kanter basert på Hamming-avstand
    E = []
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            E.append((i, j, hamming_distance(animals[i][1], animals[j][1])))

    # Finner klynger
    clusters = find_clusters(E, len(animals), k)

    # Gjøre om fra klynger basert på indekser til klynger basert på dyrenavn
    animal_clusters = [
        [animals[i][0] for i in cluster] for cluster in clusters
    ]
    return animal_clusters


tests = [
    ([("Ugle", "AGTC"), ("Ørn", "AGTA")], 2, 1),
    ([("Ugle", "CGGCACGT"), ("Elg", "ATTTGACA"), ("Hjort", "AATAGGCC")], 2, 8),
    (
        [("Ugle", "ATACTCAT"), ("Hauk", "AGTCTCAT"), ("Hjort", "CATGGCCG")],
        2,
        6,
    ),
    (
        [
            ("Ugle", "CGAAGTTA"),
            ("Hauk", "CGATGTTA"),
            ("Hamster", "AAAATCAC"),
            ("Mus", "AAAATGAC"),
        ],
        2,
        6,
    ),
    (
        [
            ("Ugle", "CAAACGAT"),
            ("Spurv", "CAGTCTAA"),
            ("Mus", "TCTGGACG"),
            ("Hauk", "CGAACTAT"),
        ],
        2,
        8,
    ),
    (
        [
            ("Ugle", "ATAACTCC"),
            ("Hauk", "TTACCTCC"),
            ("Hjort", "AGTGAACC"),
            ("Mus", "GTAGGACC"),
            ("Spurv", "ATGTCCCA"),
        ],
        3,
        4,
    ),
    (
        [
            ("Hauk", "CCTACTGATGACGCGC"),
            ("Ugle", "CCTAGTGATGAAGCAC"),
            ("Hjort", "ACTTTAACATCGCGGG"),
            ("Spurv", "ACGACTGATGAAGCAC"),
            ("Mus", "GTTAGACAATGGAGTG"),
            ("Rotte", "GTCGTACAATTGAGTG"),
        ],
        3,
        9,
    ),
    (
        [
            ("Ugle", "GGAGACCGGCTTCCTA"),
            ("Marsvin", "GCTACCTTGCTCACGT"),
            ("Hauk", "CGAGACCAGCTGCTGG"),
            ("Hjort", "GACATCTCTGTTCGGC"),
            ("Spurv", "GGAGACCGGCTTCCTG"),
            ("Rotte", "ACTACCTTGCGCACGA"),
            ("Mus", "TCTACCTTGCCCACGA"),
        ],
        3,
        10,
    ),
    (
        [
            ("Spurv", "TAGCAGTTCCTGAGAA"),
            ("Hjort", "ATGCATATCAGACGAT"),
            ("Ugle", "TAGCGATTTCAGAATT"),
            ("Rotte", "GACGGATTATTCCCCA"),
            ("Marsvin", "GAGGAATGGTAATCGC"),
            ("Hauk", "GATCGGTATCAGAACT"),
            ("Elg", "ATTCGTATAACCAAAG"),
            ("Mus", "GAGGGATGCTCCTCCC"),
        ],
        3,
        9,
    ),
    (
        [
            ("Katt", "CCGTGGTATCAAATAA"),
            ("Hjort", "TTACAGGCGGGCGTTC"),
            ("Hauk", "GGGAAATGAGCTTTCT"),
            ("Rotte", "ATCCTATAATGACCCT"),
            ("Elg", "TTGCATGCGGGCGATT"),
            ("Marsvin", "TTCGGCGGAGGTTCTA"),
            ("Mus", "ATCGGAGGAGGATCTC"),
            ("Ugle", "GGCTAGTGCGCTTTTT"),
            ("Spurv", "TGCCAGTCCGCTTTAT"),
        ],
        4,
        9,
    ),
    (
        [
            ("Hjort", "GATTACCCATGCTGGA"),
            ("Leopard", "TTTTCCTACCTAGTTA"),
            ("Ugle", "TCCCGGGAAGGGGATG"),
            ("Hauk", "TCCCAGCAAGGGGCTG"),
            ("Rotte", "CGCAGGACCGGAGGCA"),
            ("Spurv", "TCACGTGACGGGGGTG"),
            ("Katt", "TTTTCCTAACGGGTTA"),
            ("Mus", "CGCCGGAGCGAAACTA"),
            ("Elg", "GTATAGCTGTGCAGGA"),
            ("Marsvin", "AGCTGGGGCGTCAAGA"),
        ],
        4,
        9,
    ),
    (
        [
            ("Spurv", "AATCCCTGTAACGCGT"),
            ("Rotte", "CACCAGTCCGAGGAAC"),
            ("Leopard", "CACCCTATATCAAAGG"),
            ("Hauk", "AAATTGTCTCACGGGG"),
            ("Mus", "CACCACTCCTAGGAAC"),
            ("Elg", "ATGAGAGAGAGCTCCT"),
            ("Hjort", "ATGCTAGTGGGCCGCT"),
            ("Elefant", "TTTGAACAGTTTTAAT"),
            ("Marsvin", "AAGCCCTCAGAGCAAC"),
            ("Nesehorn", "TTTGACCAGTATTAAC"),
            ("Ugle", "AAAATGTCTAACGAGG"),
            ("Katt", "CACCCTATACCAAAGG"),
        ],
        5,
        9,
    ),
    (
        [
            ('aa', 'AAACTGCAGGCACCGATTTTAATGATTAACCGCGCACAGTGAC'),
            ('ab', 'TCAAAAGAGCCTGCACCGCGGCATAGGTTCGCTGACATGAAGA'),
            ('ac', 'GATTGGGTACGCCTTCAGATACTGCGATATGCTATCCCAAGTG'),
            ('ad', 'CTGACACTGAAGTGAACCGTCCGCCGCAGTGGTATGCGGCGAG'),
            ('ae', 'CCGAGGGATCCTAAAGAAGGAGCGGCTTTTCATTTGTTCGCCT'),
            ('af', 'CTCTGATCAATGCAGCCGCGTTACTATAACACGGGGCGATTAC'),
            ('ag', 'GTGAGGGTGAAAAGGGGTGGACCTACGACCGTTAAGTGCCTCG'),
            ('ah', 'CTATATGCCGAACTCTAGAGATGGACAAAGTATGACATTGGAG'),
            ('ai', 'CGCCTGCACTATTCGGGCCCAATTTTGGTATGGAGTCGTCGGT'),
            ('aj', 'GGGCACCAAGGGATTCGCTCCTAATGGCCTAAGGGGCTCAAGT'),
            ('ak', 'ACAGTACAGCCCCCCCCTCGATAGAGTCTGTTCAAGAGATTTA'),
            ('al', 'GTTTGTAGTTGAAGTAATGGCGGGATAAGGTTTAGAGGAAGGG'),
            ('am', 'TCAAGCAAATTCCAGTAGTTGAGAGAAGTACTAAAGTCTCGCC'),
            ('an', 'GGTTAACATATTATCGGTGGTAAACCATCCGATCCCACCCGAT'),
            ('ao', 'TCCGACCCTCTAGGCGTAATAGAGATGCACGACCTCCAGCAAT'),
            ('ap', 'AGACGAATCTAGAGGTCCAGGCAATCAGGCATTTCCATAGCAG'),
            ('aq', 'GGTTACGCGCTCGCATTCTGAAAAGTATTCAAGGCCAATGGGT'),
            ('ar', 'GCGATATAAGAATTAACCCTGATTCTGGGTTTGCACGCACTCT'),
            ('as', 'GAGGCTAATCTTTCATTGGAAGGCCAGGAGTGAGTAGGCCGCT'),
            ('at', 'AAGTACGAAGTCCTAGTCCGTTTGATGTATGCAATCAAGGAGT'),
            ('au', 'GCTTCGATGGTGGCCCGGGAAAGCGGCAAGAGACTTCTAAGCG'),
            ('av', 'AGCTGCATCCGCCGGAATAGGTTTTCATCTAAGGCGAACCGTT'),
            ('aw', 'ACACAACCGCCTACGTAGCCACCGATAAATCTGTCATATTATA'),
            ('ax', 'CGTGCGACGATCATGCCCCTGCGCTATAGAAACCCGTCCCCTA'),
            ('ay', 'CGACTCGATATTTGTCTGCCGGTACGGCCGGTACACCCCTATT'),
            ('az', 'TAATAAGGTTACACTGGTGACGCAGATCCAGCCGGGCGAGCTC'),
            ('ba', 'CAGTCGTCGCGCAGTCTTTGCCCCGCAACGGCCACCACGGCCC'),
            ('bb', 'CGTTGCAGCGCGACAATGATTGATAAAGGAACCGATTTACCAC'),
            ('bc', 'ACCAAGGCTTATGAGCCGCCGTGCAGTGCAGCCAGTATATTAT'),
            ('bd', 'TACCGCGACTTAGGTTATTATTAGGAGACCTGAAGGACTAACC'),
            ('be', 'GGGCGTGGCGGTCCAAGAACCACTAGGTCCTTGTGGGCAGTCT'),
            ], 
            20, 
            26,
),

]

failed = False
import itertools

for animals, k, optimal in tests:
    clusters = find_animal_groups(animals[:], k)

    test = "(animals={:}, k={:})".format(animals, k)
    if type(clusters) != list:
        print(
            "find_animal_groups skal returnere en liste av klynger. For testen "
            + "{:} gjorde ikke implementasjonen din dette. Den ".format(test)
            + "returnerte heller {:}.".format(clusters)
        )
        failed = True
        break

    if len(clusters) != k:
        print(
            "Implementasjonen din lage ikke riktig antall klynger for testen "
            + "{:}. Du lagde {:} klynger.".format(test, len(clusters))
        )
        failed = True
        break

    cluster_animals = [animal for cluster in clusters for animal in cluster]
    if len(cluster_animals) > len(animals):
        print(
            "Klyngene dine inneholder flere elementer enn det som finnes. "
            + "Du returnerte {:} for testen {:}.".format(clusters, test)
        )
        failed = True
        break

    if len(cluster_animals) > len(set(cluster_animals)):
        print(
            "Klyngene dine inneholder duplikater. Du returnerte "
            + "{:} for testen {:}.".format(clusters, test)
        )
        failed = True
        break

    if set(name for name, _ in animals) != set(cluster_animals):
        print(
            "Klyngene dine inneholder ikke alle dyrene eller inneholder også "
            + " andre dyr. Du returnerte "
            + "{:} for testen {:}.".format(clusters, test)
        )
        failed = True
        break

    lookup = {
        animal: index
        for index, cluster in enumerate(clusters)
        for animal in cluster
    }
    t = lambda x: x[0] != x[1]
    sep_dist = min(
        sum(map(t, zip(a1[1], a2[1])))
        for a1, a2 in itertools.combinations(animals, 2)
        if lookup[a1[0]] != lookup[a2[0]]
    )
    if sep_dist < optimal:
        print(
            "Klyngene har ikke maksimal separasjonsavstand. Den maksimale "
            + "seperasjonsavstanden er {:}, men koden ".format(optimal)
            + "resulterte i en seperasjonsavstand på {:} ".format(sep_dist)
            + "for testen {:}".format(test)
        )
        failed = True
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")