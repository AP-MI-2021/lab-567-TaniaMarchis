def creeazaObiect(id,nume,descriere,pret,locatie):
    '''
    creeaza un dictionar ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    '''

    return [id, nume, descriere, pret, locatie]


def getId(obiect):
    '''
    da id-ul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: id-ul obiectului
    '''

    return obiect[0]

def getNume(obiect):
    '''
    da numele unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: numele obiectului
    '''

    return obiect[1]

def getDescriere(obiect):
    '''
    da descrierea unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: descrierea obiectului
    '''

    return obiect[2]

def getPret(obiect):
    '''
    da pretul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: pretul obiectului
    '''

    return obiect[3]


def getLocatie(obiect):
    '''
    da locatia unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: locatia obiectului
    '''

    return obiect[4]

def toString(obiect):

    return "Id: {}, Nume: {}, Descriere : {}, Pret : {}, Locatie : {} ".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )