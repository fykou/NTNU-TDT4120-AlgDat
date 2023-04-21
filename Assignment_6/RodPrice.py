#!/usr/bin/env python
__author__ = "Hoyby"


def cutRod(price, n):
    if n <= 0:  # base case, hvis staven har lengde 0
        return 0  # så er prisen 0
    max_val = -1

    for i in range(0, n):  # iterer gjennom lengen av staven
        # finn max mellom max_val og et rekursivt kall som vil returnere alle kombinasjoner av staver.
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val


def bottomsUpCutRod(price, n):
    result = [0 for x in range(n + 1)]  # Løsnings-tabell, 0..n+1
    result[0] = 0  # Verdien til en stav med lenge 0 = 0

    for i in range(1, n + 1):  # For hver lenge av staven
        max_val = -1
        for j in range(i):  # Finn den optimale løsningen
            max_val = max(
                max_val, price[j] + result[i - j - 1]
            )  # her brukes del-løsningen i løsnings-tabellen
        result[i] = max_val  # Lagre del-løsning til løsnings-tabellen

    return result[n]  # Returner optimal løsning for en stav av lenge n.


def topDownRodCutting(price, n, result=None):
    if result == None:  # initialiserer løsnings-tabellen
        result = dict()
        result[0] = 0

    if n in result and result[n] >= 0:  # her brukes del-løsningen i løsnings-tabellen
        return result[n]
    max_val = -1

    for i in range(0, n):
        max_val = max(
            max_val, price[i] + topDownRodCutting(price, n - i - 1, result)
        )  # rekursivt kall for å finne optimal løsning

    result[n] = max_val  # legg til optimal løsning for hvert rekursivt kall
    return result[
        n
    ]  # Det siste kallet i call-stacken vil returnere optimal løsning for den endlige n


def extendedBottomsUpCutRod(price, n):
    result = [0 for x in range(n + 1)]  # Løsnings-tabell, 0..n+1
    result[0] = 0  # Verdien til en stav med lenge 0 = 0
    s = dict()

    for i in range(1, n + 1):  # For hver lenge av staven
        max_val = -1
        for j in range(0, i):  # Finn den optimale løsningen
            if max_val < price[j] + result[i - j - 1]:
                max_val = (
                    price[j] + result[i - j - 1]
                )  # her brukes del-løsningen i løsnings-tabellen
                s[i] = j + 1
        result[i] = max_val  # Lagre del-løsning til løsnings-tabellen

    return result, s


price = [3, 5, 10, 12, 14]
size = len(price)
print("Maximum Obtainable Value is", extendedBottomsUpCutRod(price, size))
