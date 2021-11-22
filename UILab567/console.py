from DomainLab567.obiect import toString
from LogicLab567.CRUD import adaugaObiect, stergeObiect, modificaObiect
from LogicLab567.functionalitate import mutareObiect, concatenareString, celMaiMarePretPerLocatie, ordonareDupaPret, sumaPreturilorPerLocatie


def printMenu():

    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Mutarea tuturor obiectelor dintr-o locatie in alta.")
    print("5. Concatenarea unui string la descrierile obiectelor.")
    print("6. Determinarea celui mai mare pret pentru fiecare locatie.")
    print("7. Ordonarea obiectelor crescator dupa pret.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiect.")
    print("x. Iesire.")


def uiAdaugaObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input("Dati pretul: "))
        locatie = input("Dati locatia: ")
        rezultat = adaugaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except  ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        rezultat = stergeObiect(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaObiect(lista, undoList, redoList):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatie a obiectului: ")
        rezultat = modificaObiect(id, nume, descriere, pret, locatie, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMutareObiect(lista, undoList, redoList):
    try:
        locatia1 = input("Dati locatia din care se va muta obiectul: ")
        locatia2 = input("Dati locatia in care se va muta obiectul: ")
        rezultat = mutareObiect(locatia1, locatia2, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiConcatenareString(lista, undoList, redoList):
    try:
        string = input("Dati stringul ce se va concatena in descrierea obiectului: ")
        valoare = float(input("Dati valoarea: "))
        rezultat = concatenareString(string, valoare, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiCelMaiMarePretPerLocatie(lista):

    rezultat = celMaiMarePretPerLocatie(lista)

    for locatie in rezultat:
        print("Locatia {} are pretul maxim de {}".format(locatie, rezultat[locatie]))


def uiOrdonareDupaPret(lista):

   listaOrdonata = []
   listaOrdonata = ordonareDupaPret(lista)
   showAll(listaOrdonata)

def uiSumaPreturilorPerLocatie(lista):

    rezultat = sumaPreturilorPerLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor egala cu {}".format(locatie, rezultat[locatie]))


def showAll(lista):

    for obiect in lista:
        print(toString(obiect))



def runMenu(lista):

    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaObiect(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeObiect(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaObiect(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiMutareObiect(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiConcatenareString(lista, undoList, redoList)
        elif optiune == "6":
            uiCelMaiMarePretPerLocatie(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "8":
             uiSumaPreturilorPerLocatie(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) >0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")




