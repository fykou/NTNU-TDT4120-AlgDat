#!/usr/bin/env python
__author__ = "Hoyby"

"""
Et viktig problem knyttet til organdonasjon er å sikre at at donor og mottager av et organ er kompatible.

En forenklet versjon av dette er at det finnes et antall attributter som representerer ulike biologiske og
 medisinske sider ved personene (for eksempel alder, kjønn og blodtype). Det er større sannsynlighet for en
  vellykket organtransplantasjon hvis organdonor og organmottager matcher på flest mulig av disse attributtene, 
  for ellers kan det hende at immunforsvaret til mottageren ødelegger det nye organet, en såkalt avstøtningsreaksjon.

Av erfaring er det lav sannsynlighet for at kroppen avstøter seg det nye organet dersom donor og mottager matcher på minst kk attributter.

En måte å representere dette på er som en graf, der det er en kant fra donor til mottager dersom de har minst kk attributter til felles. 
Vi skal se i forelesning 12 at dersom vi har en slik graf kan vi enkelt finne en matching mellom donorer og mottagere, 
slik at flest mulig mottagere får en kompatibel donor.

Du skal implementere funksjonen compatibility_graph(donors, recipients, k). 
Her er donors og recipients lister av attributtene til henholdsvis donorer og mottagere: donors[i][j] er det jj-te attributtet 
(representert ved en tekststreng) til den ii-te donoren og tilsvarende for recipients[i][j]. Listene har attributtene i samme rekkefølge, 
så en donor dd og en mottager mm har et matchende attributt jj dersom donors[d][j] == recipients[m][j]. 
Antallet attributter som må matche for at en donor og en mottager skal sees på som kompatible er gitt ved k.

Funksjonen skal returnere en liste donor_edges der donor_edges[i] er en liste over alle
 mottagere (gitt ved deres indeks i recipients) som donor ii-te er kompatibel med.
"""


def compatibility_graph(donors, recipients, k):
    donor_edges = []  # Initialize returning list of compatible donors - recipents
    for i in range(0, len(donors)):
        recipientIndex = -1
        donor_edges.append([])  # Add new list for each donor
        for j in range(0, len(recipients)):
            recipientIndex += 1
            count = 0  # Start new count for attributes
            for donorAttribute in donors[i]:
                if (
                    recipientIndex not in donor_edges[i] and k == 0
                ):  # If no requirement for number of matches, do:
                    donor_edges[i].append(recipientIndex)
                elif donorAttribute in recipients[j]:  # If matching attributes found:
                    count += 1
                    if recipientIndex not in donor_edges[i] and count >= k:
                        donor_edges[i].append(recipientIndex)

    return donor_edges


# def compatibility_graph(donors, recipients, k):
#     donor_edges = [] # Initialize returning list of compatible donors - recipents
#     donorIndex = -1
#     for donor in donors:
#         donorIndex += 1
#         recipientIndex = -1
#         donor_edges.append([]) # Add new list for each donor
#         for recipient in recipients:
#             recipientIndex += 1
#             count = 0 # Start new count for attributes
#             for donorAttribute in donor:
#                 for recipientAttribute in recipient:
#                     if k == 0: # If no requirement for number of matches, do:
#                         donor_edges[donorIndex].append(recipientIndex)
#                     elif donorAttribute == recipientAttribute: # If matching attributes found:
#                         count += 1
#                         if recipientIndex not in donor_edges[donorIndex] and count >= k:
#                             donor_edges[donorIndex].append(recipientIndex)
#     return donor_edges

tests = [
    (([], [], 0), []),
    (([["ab"]], [], 0), [[]]),
    (([], [["ab"]], 0), []),
    (([["ab"]], [["ab"]], 1), [[0]]),
    (([["ab"]], [["ac"]], 1), [[]]),
    (([["ab"]], [["ac"]], 0), [[0]]),
    (([["ab"]], [["ac"], ["ab"]], 1), [[1]]),
    (([["ab"], ["ac"]], [["ab"]], 1), [[0], []]),
    (([["ab"], ["ac"]], [["ac"], ["ab"]], 1), [[1], [0]]),
    (([["ab"], ["ac"]], [["ac"], ["ab"]], 0), [[0, 1], [0, 1]]),
    (
        ([["IRk", "s", "S", "9zF"], ["ac"]], [["IRk", "s", "S", "9zF"], ["ab"]], 0),
        [[0, 1], [0, 1]],
    ),
    (
        ([["ab", "12"], ["ac", "22"]], [["ab", "22"], ["ac", "22"]], 2),
        [[], [1]],
    ),
    (([], [[], []], 1), []),
    (
        (
            [],
            [
                ["IRk", "s", "S", "9zF"],
                ["V2xa", "JqZV", "PxbUl", "WbKZw"],
                ["V2xa", "s", "PxbUl", "7NoD"],
            ],
            2,
        ),
        [],
    ),
    (
        (
            [["dwfAa", "bt7c", "d1iP"], ["dwfAa", "bt7c", "d1iP"]],
            [
                ["dwfAa", "H", "vN82"],
                ["dwfAa", "bt7c", "vN82"],
                ["dwfAa", "H", "vN82"],
            ],
            4,
        ),
        [[], []],
    ),
    (
        ([["oLfIi", "wPAw"], ["gTnJf", "wPAw"], ["gTnJf", "LERhd"]], [], 1),
        [[], [], []],
    ),
    (
        ([["uw"], ["uw"], ["Lb"], ["uw"]], [["4r7lb"], ["Lb"]], 1),
        [[], [], [1], []],
    ),
    (([["wcaP", "zXgJ"]], [], 1), [[]]),
    (([], [], 1), []),
    (
        (
            [["w", "oA", "oIa"]],
            [["w", "oA", "oIa"], ["d", "oA", "vodI"], ["w", "oA", "5"]],
            1,
        ),
        [[0, 1, 2]],
    ),
    (([], [["x", "7HyQl", "Wr38", "Ww"], ["x", "7HyQl", "yq", "Ww"]], 9), []),
    (([["rX1", "z"], ["rX1", "ZY2w"]], [["qX1Ph", "7a0M"]], 1), [[], []]),
    (
        (
            [["KAy3Z", "b"], ["KAy3Z", "b"], ["KAy3Z", "b"]],
            [["KAy3Z", "b"], ["KAy3Z", "b"]],
            2,
        ),
        [[0, 1], [0, 1], [0, 1]],
    ),
    (
        (
            [["a", "b"], ["a", "b"], ["a", "b", "c", "d"], ["c", "d", "e"]],
            [["a", "b"], ["a", "b"], ["c", "d", "e"], ["a"], ["a", "c"]],
            2,
        ),
        [[0, 1], [0, 1], [0, 1, 2, 4], [2]],
    ),
]


for test_case, answer in tests:
    donors, recipients, k = test_case
    student = compatibility_graph(donors, recipients, k)
    if len(student) != len(answer) or not all(
        [sorted(stu) == ans for stu, ans in zip(student, answer)]
    ):
        response = (
            "Koden feilet for følgende input: "
            + "(donors={:}, recipients={:}, k={:}). ".format(donors, recipients, k)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        print(response)
        break
