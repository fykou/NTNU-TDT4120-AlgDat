#!/usr/bin/env python
__author__ = "Hoyby"

"""
Trær har mange praktiske anvendelser. En av anvendelsene er å analysere lange strenger. 
Dette gjelder spesielt når det kommer til genanalyse, siden DNA er veldig langt, 
og man trenger derfor raske algoritmer for å gjøre slike analyser mulig.

I denne oppgaven skal du slå opp i et tre for å se om en viss DNA-sekvens er sett før.

Treet består av Node-objekter, en type som er laget for deg.

Disse objektene har to attributter:

children er en oppslagstabell (dictionary) med alle nodebarna til noden. Den angir kobling mellom bokstav og node. 
For å gå til et barn kan man skrive currentnode = currentnode.children['A'], 
gitt currentnode er den nåværende noden og at denne noden har et barn "A".
count er et heltall som holder styr på hvor mange DNA-sekvenser det finnes i databasen av den korresponderende strengen til noden. 
Den korresponderende strengen er strengen som dannes av bokstavene langs stien fra rotnoden ned denne noden.
Treet kan se ut som følgende. Her ser vi at det finnes 1 forekomst av DNA-sekvensen "AAG", 
4 forekomster av "C" og 0 forekomster av "CT".


Din oppgave er å implementere funksjonen search_tree(root, dna). 
root er Node-objektet i roten av treet, mens dna er tekststrengen (altså DNA-sekvensen) du skal søke etter. 
Funksjonen skal returnere hvor mange forekomster det er i databasen av denne strengen.
"""


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

    def __str__(self):
        return (
            f"{{count: {self.count}, children: {{"
            + ", ".join([f"'{c}': {node}" for c, node in self.children.items()])
            + "}}"
        )

    @classmethod
    def from_string(cls, s):
        node = Node()
        ind = 0
        ind = s.index("count") + len("count: ")
        ind2 = s.index(",", ind)
        node.count = int(s[ind:ind2])
        ind = s.index("{", ind) + 1
        while ind != len(s) - 2:
            ind = s.index("'", ind) + 1
            c = s[ind]
            ind = s.index("{", ind)
            ind2 = ind + 1
            count = 1
            while count:
                if s[ind2] == "{":
                    count += 1
                if s[ind2] == "}":
                    count -= 1
                ind2 += 1
            node.children[c] = Node.from_string(s[ind:ind2])
            ind = ind2
        return node


"""def search_tree(root, dna):
    count = 0               
    if root != None:
        if dna == "":       
            return root.count
            
        dnaList = []    
        for ch in dna:      #changes string into list of letters, except empty string
            if ch == "":
                continue
            dnaList.append(ch)
      
        for i in dnaList:
            node = None                     #start none as None
            if i in root.children:          #if letter in dnaList is a child of root, then set node as that child
                node = root.children[i]
            count += search_tree(node, ''.join(dnaList[1:]))    #increase count by doing same function over with one less letter in the dna string
            dnaList = dnaList[1:]           #shorten the list for that first letter
    return count"""


"""def search_tree(root, dna): #v2
    count = 0              
    if dna == "":       
        return root.count
        
    dnaList = []    
    for ch in dna:     
        if ch == "":
            continue
        dnaList.append(ch)
    
    for dna in dnaList:
        node = Node()                   #empty node with count = 0 and children = {}                
        if dna in root.children:          #if letter in dnaList is a child of root, then set node as that child
            node = root.children[dna]
        dnaList = dnaList[1:]           #remove first letter from list (since we've used it)
        count += search_tree(node, ''.join(dnaList))    #increase count by doing same function over with one less letter in the dna string
    return count"""


def search_tree(root, dna):  # v3
    dnaList = []
    for ch in dna:
        dnaList.append(ch)

    for dna in dnaList:
        if dna not in root.children.keys():
            return 0
        root = root.children[dna]

    return root.count


tests = [
    (("{count: 1, children: {}}", ""), 1),
    (("{count: 0, children: {}}", ""), 0),
    (("{count: 1, children: {}}", "A"), 0),
    (("{count: 2000, children: {}}", ""), 2000),
    (("{count: 0, children: {'A': {count: 1, children: {}}}}", ""), 0),
    (("{count: 0, children: {'A': {count: 2, children: {}}}}", "A"), 2),
    (
        (
            "{count: 0, children: {'A': {count: 0, children: {'A': {count: 2, children: {}}}}}}",
            "A",
        ),
        0,
    ),
    (
        (
            "{count: 0, children: {'A': {count: 0, children: {'A': {count: 2, children: {}}}}}}",
            "B",
        ),
        0,
    ),
    (
        (
            "{count: 0, children: {'A': {count: 0, children: {'A': {count: 2, children: {}}}}}}",
            "AA",
        ),
        2,
    ),
    (("{count: 0, children: {}}", ""), 0),
    (
        (
            "{count: 1, children: {'T': {count: 0, children: {'G': {count: 0, children: {'C': {count: 1, children: {}}}}}}, 'A': {count: 0, children: {'C': {count: 1, children: {}}}}}}",
            "AC",
        ),
        1,
    ),
    (
        (
            "{count: 1, children: {'G': {count: 0, children: {'A': {count: 0, children: {'A': {count: 0, children: {'G': {count: 1, children: {}}}}}}}}}}",
            "",
        ),
        1,
    ),
    (("{count: 0, children: {}}", "GCAAC"), 0),
    (("{count: 0, children: {}}", "TGC"), 0),
    (
        (
            "{count: 0, children: {'T': {count: 0, children: {'T': {count: 0, children: {'C': {count: 0, children: {'A': {count: 1, children: {}}}}}}, 'G': {count: 1, children: {}}}}}}",
            "TCTCT",
        ),
        0,
    ),
    (
        (
            "{count: 0, children: {'A': {count: 0, children: {'C': {count: 0, children: {'C': {count: 0, children: {'T': {count: 0, children: {'A': {count: 1, children: {}}}}}}}}}}, 'T': {count: 0, children: {'C': {count: 2, children: {}}}}}}",
            "TGA",
        ),
        0,
    ),
    (("{count: 0, children: {}}", ""), 0),
    (
        (
            "{count: 0, children: {'T': {count: 0, children: {'C': {count: 0, children: {'T': {count: 0, children: {'C': {count: 1, children: {}}}}}}}}, 'G': {count: 1, children: {}}}}",
            "TCTC",
        ),
        1,
    ),
    (("{count: 0, children: {'C': {count: 1, children: {}}}}", "CAA"), 0),
]


for test_case, answer in tests:
    root, dna = test_case
    root = Node.from_string(root)
    student = search_tree(root, dna)
    if student != answer:
        print(
            "Koden feilet for følgende input: "
            + '(root={:}, dna="{:}"). '.format(root, dna)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        break
