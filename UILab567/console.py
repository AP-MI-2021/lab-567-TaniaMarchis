from DomainLab567.obiect import toString
from LogicLab567.CRUD import adaugaObiect, stergeObiect, modificaObiect



def printMenu():

    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("a. Afisare obiect")
    print("x. Iesire")


def uiAdaugaObiect(lista):

    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul: "))
    locatie = input("Dati locatia: ")
    return adaugaObiect(id, nume, descriere, pret, locatie, lista)

def uiStergeObiect(lista):

    id = input("Dati id-ul obiectului de sters: ")
    return stergeObiect(id, lista)

def uiModificaObiect(lista):

    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float(input("Dati noul pret: "))
    locatie = input("Dati noua locatie a obiectului: ")
    return modificaObiect(id, nume, descriere, pret, locatie, lista)


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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")



