from DomainLab567.obiect import getId, getNume, getDescriere, getPret, getLocatie
from LogicLab567.CRUD import adaugaObiect
from LogicLab567.functionalitate import mutareObiect, concatenareString


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


