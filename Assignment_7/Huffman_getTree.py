#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
I denne oppgaven får du et huffmantre og skal hente ut kodingen til de ulike tegnene.

Treet er representert ved et objekt av type Node med attributter left_child og right_child for venstre og høyre barnenode. 
Disse er satt til None hvis noden ikke har noen barnenoder (husk at et huffmantre er et fullt binærtre, 
så enten har en node to eller ingen barnenoder). I tillegg har Node et attributt character som er tegnet noden representerer. 
Dette attributtet er kun satt i løvnodene, siden det kun er de som representerer et tegn.

Du skal implementere funksjonen encoding(node) som tar inn node som er et objekt av type Node, som forklart over. 
Denne noden er rotnoden i et huffmantre. Funksjonen skal returnere en oppslagstabell med tegn som nøkler og strenger med kun «0» og «1» som verdier, 
hvor disse strengene er kodene til de tilsvarende tegnene.

Vi følger lærebokas konvensjon om at kanten til venstre barnenode tilsvarer «0» og kanten til høyre barnenode tilsvarer «1».

Hvis treet funksjonen får inn er dette:


så skal encoding returnere {"n": "00", "b": "01", "a": "1"}.
'''


# def encoding(node, result = None):
#     if result == None:
#         result = {}

#     # Check left
#     if node.left_child != None:
#         if node.character in result:
#             result[node.left_child.character] = result[node.character] + '0'
#         else:
#             result[node.left_child.character] = '0'
#         encoding(node.left_child, result)

#     # Check right
#     if node.right_child != None:
#         if node.character in result:
#             result[node.right_child.character] = result[node.character] + '1'
#         else:
#             result[node.right_child.character] = '1'
#         encoding(node.right_child, result)

#     # Delete empty nodes from result
#     if node.character == None and None in result:
#         del result[node.character]

#     return result

def encoding(node):
    code = {}
    traverseTreeEdges(node, code)
    return code
 
def traverseTreeEdges(root, code, value="", string =""):
    if value == "left":
        string += "0"
    elif value == "right":
        string += "1"
    if root != None:
        traverseTreeEdges(root.left_child, code, "left", string)
        if root.character != None:
            code[root.character] = string
        traverseTreeEdges(root.right_child, code, "right", string)
        if root.character != None:
            code[root.character] = string
    return string
    


tests = [
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "n",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "character": None,
        },
        {"n": "0", "a": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "n",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "character": None,
            },
            "character": None,
        },
        {"n": "0", "a": "10", "b": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "c",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "character": None,
            },
            "character": None,
        },
        {"c": "0", "a": "10", "b": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "c",
            },
            "character": None,
        },
        {"a": "0", "c": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "c",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"a": "0", "b": "10", "c": "110", "d": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "c",
                },
                "character": None,
            },
            "character": None,
        },
        {"a": "0", "b": "100", "d": "101", "c": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "a",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "c",
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "d",
            },
            "character": None,
        },
        {"a": "000", "b": "001", "c": "01", "d": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "X",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "f",
            },
            "character": None,
        },
        {"X": "0", "f": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "X",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "B",
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "character": None,
        },
        {"X": "00", "B": "01", "a": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "K",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "B",
            },
            "character": None,
        },
        {"K": "0", "B": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "Y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "F",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "O",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "M",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "Q",
                },
                "character": None,
            },
            "character": None,
        },
        {"Y": "00", "F": "01", "O": "100", "M": "101", "Q": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "F",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "s",
            },
            "character": None,
        },
        {"F": "0", "s": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "S",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "O",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"S": "0", "z": "10", "b": "110", "O": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "R",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "e",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "T",
                },
                "character": None,
            },
            "character": None,
        },
        {"R": "0", "e": "10", "T": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "B",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "d",
                },
                "character": None,
            },
            "character": None,
        },
        {"B": "0", "y": "10", "d": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "u",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "q",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "character": None,
            },
            "character": None,
        },
        {"u": "0", "q": "10", "z": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "i",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "J",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "I",
                },
                "character": None,
            },
            "character": None,
        },
        {"i": "0", "J": "10", "I": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "T",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "K",
            },
            "character": None,
        },
        {"T": "0", "K": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "x",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "S",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "h",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"x": "0", "S": "10", "d": "110", "h": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "t",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "d",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "L",
                },
                "character": None,
            },
            "character": None,
        },
        {"y": "00", "t": "01", "d": "10", "L": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "w",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "p",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "S",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "K",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"w": "0", "p": "10", "S": "110", "K": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "u",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "U",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "character": None,
            },
            "character": None,
        },
        {"y": "00", "u": "01", "U": "10", "a": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "e",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "O",
                },
                "character": None,
            },
            "character": None,
        },
        {"e": "0", "z": "10", "O": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "s",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "S",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "l",
                },
                "character": None,
            },
            "character": None,
        },
        {"s": "0", "S": "10", "l": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "g",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "E",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "i",
                    },
                    "character": None,
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "U",
            },
            "character": None,
        },
        {"g": "00", "E": "010", "i": "011", "U": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "G",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "W",
            },
            "character": None,
        },
        {"G": "0", "W": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "A",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "E",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "k",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "a",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"A": "0", "E": "10", "k": "110", "a": "111"},
    ),
]


class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.character = None

    def __str__(self):
        return (
            f'{{ "left_child": {self.left_child}, "right_child": {self.right_child}, "character": '
            + (
                '"' + self.character + '"'
                if self.character is not None
                else "None"
            )
            + "}"
        )

    @classmethod
    def from_dict(cls, dic):
        node = Node()
        if dic["left_child"] is not None:
            node.left_child = Node.from_dict(dic["left_child"])
        if dic["right_child"] is not None:
            node.right_child = Node.from_dict(dic["right_child"])
        node.character = dic["character"]
        return node


for test_case, answer in tests:
    node = Node.from_dict(test_case)
    student = encoding(node)
    if student != answer:
        response = "Koden feilet for følgende input: (data={:}). ".format(
            node
        ) + "Din output: {:}. Riktig output: {:}".format(student, answer)
        print(response)
        break