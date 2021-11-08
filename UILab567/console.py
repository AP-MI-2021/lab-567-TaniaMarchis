from DomainLab567.obiect import toString
from LogicLab567.CRUD import adaugaObiect, stergeObiect, modificaObiect
from LogicLab567.functionalitate import mutareObiect, concatenareString


def printMenu():

    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta.")
    print("5. Concatenarea unui string la descrierile obiectelor.")
    print("a. Afisare obiect.")
    print("x. Iesire.")


def uiAdaugaObiect(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input("Dati pretul: "))
        locatie = input("Dati locatia: ")
        return adaugaObiect(id, nume, descriere, pret, locatie, lista)
    except  ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeObiect(lista):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        return stergeObiect(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaObiect(lista):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie a obiectului: ")
        return modificaObiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMutareObiect(lista):
    try:
        locatia1 = input("Dati locatia din care se va muta obiectul: ")
        locatia2 = input("Dati locatia in care se va muta obiectul: ")
        return mutareObiect(locatia1, locatia2, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiConcatenareString(lista):
    try:
        string = input("Dati stringul ce se va concatena in descrierea obiectului: ")
        valoare = float(input("Dati valoarea: "))
        return concatenareString(string, valoare, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):

    for obiect in lista:
        print(toString(obiect))



def runMenu(lista):

    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaObiect(lista)
        elif optiune == "2":
            lista = uiStergeObiect(lista)
        elif optiune == "3":
            lista = uiModificaObiect(lista)
        elif optiune == "4":
            lista = uiMutareObiect(lista)
        elif optiune == "5":
            lista = uiConcatenareString(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")




