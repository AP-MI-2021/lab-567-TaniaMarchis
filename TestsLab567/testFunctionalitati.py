from DomainLab567.obiect import getId, getNume, getDescriere, getPret, getLocatie
from LogicLab567.CRUD import adaugaObiect, modificaObiect, stergeObiect
from LogicLab567.functionalitate import mutareObiect, concatenareString, celMaiMarePretPerLocatie, ordonareDupaPret, sumaPreturilorPerLocatie


def testMutareObiect():
    lista = []

    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    lista = adaugaObiect("3", "laptop", "Asus", 3000, "Cluj", lista)

    lista = mutareObiect("Bucuresti", "Cluj", lista)

    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "laptop"
    assert getDescriere(lista[0]) == "Huawei"
    assert getPret(lista[0]) == 4000
    assert getLocatie(lista[0]) == "Cluj"

    assert getId(lista[1]) == "2"
    assert getNume(lista[1]) == "telefon"
    assert getDescriere(lista[1]) == "iphone"
    assert getPret(lista[1]) == 2000
    assert getLocatie(lista[1]) == "Sibiu"

    assert getId(lista[2]) == "3"
    assert getNume(lista[2]) == "laptop"
    assert getDescriere(lista[2]) == "Asus"
    assert getPret(lista[2]) == 3000
    assert getLocatie(lista[2]) == "Cluj"



def testConcatenareString():

    lista = []

    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    lista = adaugaObiect("3", "laptop", "Asus", 3000, "Cluj", lista)

    lista = concatenareString("bun", 2500, lista)

    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "laptop"
    assert getDescriere(lista[0]) == "Huawei bun"
    assert getPret(lista[0]) == 4000
    assert getLocatie(lista[0]) == "Bucuresti"

    assert getId(lista[1]) == "2"
    assert getNume(lista[1]) == "telefon"
    assert getDescriere(lista[1]) == "iphone"
    assert getPret(lista[1]) == 2000
    assert getLocatie(lista[1]) == "Sibiu"

    assert getId(lista[2]) == "3"
    assert getNume(lista[2]) == "laptop"
    assert getDescriere(lista[2]) == "Asus bun"
    assert getPret(lista[2]) == 3000
    assert getLocatie(lista[2]) == "Cluj"


def testCelMaiMarePretPerLocatie():

    lista = []

    lista = adaugaObiect("1", "laptop", "Huawei", 3000, "Cluj", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 1000, "Sibiu", lista)
    lista = adaugaObiect("3", "laptop", "Asus", 2000, "Cluj", lista)

    rezultat = celMaiMarePretPerLocatie(lista)

    assert len(rezultat) == 2
    assert rezultat["Cluj"] == 3000
    assert rezultat["Sibiu"] == 1000


def testOrdonareDupaPret():

    lista = []

    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    lista = adaugaObiect("3", "laptop", "Asus", 3000, "Cluj", lista)

    rezultat = ordonareDupaPret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"


def testSumaPreturilorPerAn():

    lista = []

    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Cluj", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    lista = adaugaObiect("3", "telefon", "samsung", 3000, "Cluj", lista)
    lista = adaugaObiect("4", "televizor", "samsung", 3000, "Sibiu", lista)

    rezultat = sumaPreturilorPerLocatie(lista)

    assert rezultat["Cluj"] == 7000
    assert rezultat["Sibiu"] == 5000


def testMutareObiectUndoRedo():

    lista = [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]
    undoList = []
    redoList = []

    rezultat = mutareObiect("Cluj", "Sibiu", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 0
    assert len(redoList) == 1

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 0
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Sibiu"]]


def testConcatenareStringUndoRedo():

    lista = [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]
    undoList = []
    redoList = []

    rezultat = concatenareString("bun", 2500, lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = concatenareString("nou", 3500, lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 3
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 0
    assert len(redoList) == 2

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 1
    assert lista == [["1", "laptop", "Huawei bun", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus bun", 3000, "Cluj"]]


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 2
    assert len(redoList) == 0
    assert lista == [["1", "laptop", "Huawei bun nou", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus bun", 3000, "Cluj"]]


