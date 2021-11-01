from DomainLab567.obiect import creeazaObiect, getId, getNume, getDescriere, getPret, getLocatie


def testObiect():
    obiect = creeazaObiect("1", "laptop", "Huawei", 4000, "Bucuresti" )

    assert getId(obiect) == "1"
    assert getNume(obiect) == "laptop"
    assert getDescriere(obiect) == "Huawei"
    assert getPret(obiect) == 4000
    assert getLocatie(obiect) == "Bucuresti"