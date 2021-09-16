#!/usr/bin/env python
__author__ = "Alex Høyby"

'''
Har du noen gang trengt å installere pakker med hjelp av et pakkesystem?
 En «pakke» er her programvare som installeres på datamaskinen. 
 Python har for eksempel pakkesystemet «pip» som sin standard. 
 Populære språkuavhengige pakkesystemer er APT, Homebrew og Chocolatey.

En ting som gjør prosessen komplisert er at en pakke kan avhenge av at andre pakker er installert for at den selv kan installeres. 
Disse andre pakkene kan igjen avhenge av at andre pakker er installert. 
På den måten kan man risikere å måtte installere veldig mange pakker. 
Heldigvis har vi ikke sykliske avhengigheter, siden det da ville ha vært umulig å installere pakken.

Her skal du implementere et forenklet pakkesystem. 
Du må implementere funksjonen resolve_and_install(package) som er en funksjon som kalles når brukeren ønsker å installere en pakke. 
Her er package et Package-objekt som representer en pakke klienten ønsker å installere. 
Et Package-objekt har attributtene dependencies, som er et tuppel med Package-objekter pakken avhenger av, 
og is_installed som er en boolsk variabel som sier om pakken allerede er installert. 
Flere av pakkene kan allerede være installert før resolve_and_install kalles. 
Du kan anta at om en pakke er installert, så er alle pakkene den avhenger av også installert.

Funksjonen resolve_and_install(package) skal sørge for å installere pakken brukeren ønsker å installere. 
For å gjøre det, finnes det funksjon install(package) (som vi gir til dere) som faktisk installerer pakken på maskinen, 
men det er to regler resolve_and_install må følge når den kaller install(package):

package kan ikke allerede være installert.
Alle pakkene som package er avhengig av må være installerte.
'''


import random
import string


def resolve_and_install(package):

    if not package.is_installed:
        for dep in package.dependencies:
            resolve_and_install(dep)
        install(package)


# Hvis du ønsker nye tester, så endre dette tallet.
random.seed(123)


class Package:
    def __init__(self, dependencies, is_installed_func):
        self.__is_installed_func = is_installed_func
        self.__dependencies = dependencies

    @property
    def dependencies(self):
        return self.__dependencies

    @property
    def is_installed(self):
        return self.__is_installed_func(self)

    def __str__(self):
        return str(
            {
                "is_installed": self.is_installed,
                "dependencies": self.dependencies,
            }
        )

    def __repr__(self):
        return str(self)


def get_install_func(installed_packages):
    def install(package):
        if package.is_installed:
            raise ValueError(
                'Du kjører "install" på en pakke som allerede er installert.'
            )
        if not all([p.is_installed for p in package.dependencies]):
            raise ValueError(
                'Du kjører "install" på en pakke uten å ha installert alle pakkene den er avhengig av.'
            )
        installed_packages.add(package)

    return install


def generate_random_test(num_nodes, p):
    installed_packages = set()
    is_installed_func = lambda x: x in installed_packages
    packages = [None for i in range(num_nodes)]
    incoming_edges = [[] for i in range(num_nodes)]
    installed_limit = random.randint(0, num_nodes)
    for i in range(1, num_nodes):
        predecessors = random.sample(
            range(0, i), k=random.randint(1, min(i, max(1, int(2 * p * i))))
        )
        for pre in predecessors:
            incoming_edges[pre].append(i)
    for i in range(num_nodes - 1, -1, -1):
        dependencies = tuple([packages[j] for j in incoming_edges[i]])
        packages[i] = Package(dependencies, is_installed_func)
        if i >= installed_limit:
            installed_packages.add(packages[i])
    return (packages[0], get_install_func(installed_packages))


def generate_install_tests():
    # Some small random tests
    for i in range(100):
        yield generate_random_test(random.randint(1, 5), 0.5)


for package, install_func in generate_install_tests():
    global install
    install = install_func
    try:
        resolve_and_install(package)
    except ValueError as e:
        response = str(e) + " Input: {:}".format(package)
        print(response)
        break
    if not package.is_installed:
        response = "Pakken er ikke installert. Input: {:}".format(package)
        print(response)
        break