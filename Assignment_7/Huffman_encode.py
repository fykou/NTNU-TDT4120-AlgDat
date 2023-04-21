#!/usr/bin/env python
__author__ = "Hoyby"

"""
Huffmankoding brukes til å komprimere data, som kan spare en for store ressurser ved overføring og lagring av store datamengder.

I denne oppgaven skal du implementere en forenklet versjon av huffmankoding. 
For enkelhets skyld skal kodingen her være en binær tekststreng (det vil si en tekststring kun bestående av «0» og «1»).

Du skal implementere funksjonen encode(data, encoding). 
Her er data en tilfeldig tekststreng og encoding er en oppslagstabell (dictionary) der nøklene er 
de ulike tegnene som finnes og verdiene er de tilsvarende binære tekststrengene (som representerer en ekte huffmankoding). 
Funksjonen skal returnere den kodede strengen som tilsvarer data.

Et eksempel er om data = "nabn" og encoding = {"n": "1", "a": "00", "b": "01"}, så skal funksjonen din returnere "100011".
"""


def encode(data, encoding):
    result = ""

    for letter in data:
        result += encoding.get(letter)

    return result


# Some custom made tests
tests = [
    (("na", {"n": "0", "a": "1"}), "01"),
    (("na", {"n": "1", "a": "0"}), "10"),
    (("nabn", {"n": "1", "a": "01", "b": "10"}), "101101"),
    (("abccba", {"a": "00", "b": "01", "c": "1"}), "0001110100"),
    (("accca", {"c": "0", "a": "1"}), "10001"),
    (("abbca", {"a": "01", "b": "1", "c": "00"}), "01110001"),
    (("ffXf", {"X": "0", "f": "1"}), "1101"),
    (("iidvvv", {"v": "0", "d": "10", "i": "11"}), "111110000"),
    (("gaaCa", {"g": "00", "C": "01", "a": "1"}), "0011011"),
    (
        ("qtqXctqqX", {"q": "0", "X": "10", "c": "110", "t": "111"}),
        "01110101101110010",
    ),
    (
        (
            "MYQOIQIMMQ",
            {"I": "00", "Y": "010", "O": "011", "M": "10", "Q": "11"},
        ),
        "1001011011001100101011",
    ),
    (("zzJzv", {"J": "00", "v": "01", "z": "1"}), "1100101"),
    (("aaxaaxx", {"x": "0", "a": "1"}), "1101100"),
    (
        (
            "UIoIUIUEEl",
            {"E": "00", "o": "010", "l": "011", "U": "10", "I": "11"},
        ),
        "1011010111011100000011",
    ),
    (("GgwGN", {"g": "00", "w": "01", "N": "10", "G": "11"}), "1100011110"),
    (("EEucu", {"u": "0", "c": "10", "E": "11"}), "11110100"),
    (("RTQTj", {"R": "00", "Q": "01", "j": "10", "T": "11"}), "0011011110"),
    (("XsXPP", {"P": "0", "s": "10", "X": "11"}), "11101100"),
    (("diDDDiiD", {"D": "0", "d": "10", "i": "11"}), "101100011110"),
    (("HHuGuHu", {"u": "0", "G": "10", "H": "11"}), "11110100110"),
    (("uqzq", {"q": "0", "u": "10", "z": "11"}), "100110"),
    (("rKr", {"K": "0", "r": "1"}), "101"),
    (("YYiEEEY", {"E": "0", "i": "10", "Y": "11"}), "11111000011"),
    (("iONONNO", {"N": "0", "i": "10", "O": "11"}), "10110110011"),
    (("QuQuuxu", {"x": "00", "Q": "01", "u": "1"}), "0110111001"),
    (("yGGyy", {"G": "0", "y": "1"}), "10011"),
]


for test_case, answer in tests:
    data, encoding = test_case
    student = encode(data, encoding)
    if student != answer:
        response = (
            "Koden feilet for følgende input: "
            + "(data={:}, encoding={:}). ".format(data, encoding)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        print(response)
        break
