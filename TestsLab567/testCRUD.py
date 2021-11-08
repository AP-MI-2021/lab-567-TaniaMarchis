from DomainLab567.obiect import  getId, getNume, getDescriere, getPret, getLocatie
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




