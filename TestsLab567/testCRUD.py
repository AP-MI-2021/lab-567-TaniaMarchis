from DomainLab567.obiect import getId, getNume, getDescriere, getPret, getLocatie
from LogicLab567.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect

def testAdaugaObiect():

    lista=[]
    lista=adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "laptop"
    assert getDescriere(getById("1", lista)) == "Huawei"
    assert getPret(getById("1", lista)) == 4000
    assert getLocatie(getById("1", lista)) == "Bucuresti"


def testStergeObiect():

    lista = []
    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)

    lista = stergeObiect("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None




def testModificaObiect():

    lista = []
    lista = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    lista = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)

    lista = modificaObiect("1", "laptop", "Asus", 3000, "Cluj", lista)

    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "laptop"
    assert getDescriere(lista[0]) == "Asus"
    assert getPret(lista[0]) == 3000
    assert getLocatie(lista[0]) == "Cluj"


def testUndoRedo():

    lista = []
    undoList = []
    redoList = []

    rezultat = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0

    rezultat = adaugaObiect("3", "laptop", "asus", 3000, "Cluj", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0

    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"], ["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [["1", "laptop", "Huawei", 4000, "Bucuresti"]]]
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 2

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 3

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 3

    rezultat = adaugaObiect("1", "laptop", "Huawei", 4000, "Bucuresti", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = adaugaObiect("2", "telefon", "iphone", 2000, "Sibiu", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0

    rezultat = adaugaObiect("3", "laptop", "asus", 3000, "Cluj", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat

    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"], ["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [["1", "laptop", "Huawei", 4000, "Bucuresti"]]]
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 2

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1

    if len(redoList) > 0:
        undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[], [["1", "laptop", "Huawei", 4000, "Bucuresti"]]]
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1


    if len(undoList) > 0:
        redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[]]
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 2


    rezultat = adaugaObiect("4", "telefon", "samsung", 2500, "Cluj", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"], ["4", "telefon", "samsung", 2500, "Cluj"]]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert undoList == [[], [["1", "laptop", "Huawei", 4000, "Bucuresti"]]]
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 2

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 1
    assert len(undoList) == 1


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 0
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"], ["4", "telefon", "samsung", 2500, "Cluj"]]


def testStergereUndoRedo():

    lista = [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]
    undoList = []
    redoList = []

    rezultat = stergeObiect("2", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 2
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = stergeObiect("1", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 1
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert len(lista) == 2
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
    assert len(lista) == 2
    assert len(undoList) == 1
    assert len(redoList) == 1


def testModificareUndoRedo():


    lista = [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "iphone", 2000, "Sibiu"],["3", "laptop", "asus", 3000, "Cluj"]]
    undoList = []
    redoList = []

    rezultat = modificaObiect("2", "telefon", "samsung", 2500, "Bucuresti", lista)
    undoList.append(lista)
    redoList.clear()
    lista = rezultat
    assert len(lista) == 3
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = modificaObiect("1", "laptop", "Asus", 4500, "Oradea", lista)
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
    assert lista == [["1", "laptop", "Huawei", 4000, "Bucuresti"],["2", "telefon", "samsung", 2500, "Bucuresti"],["3", "laptop", "asus", 3000, "Cluj"]]












