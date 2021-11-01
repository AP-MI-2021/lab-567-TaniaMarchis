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

    return {
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie


    }

def getId(obiect):
    '''
    da id-ul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: id-ul obiectului
    '''

    return obiect["id"]

def getNume(obiect):
    '''
    da numele unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: numele obiectului
    '''

    return obiect["nume"]

def getDescriere(obiect):
    '''
    da descrierea unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: descrierea obiectului
    '''

    return obiect["descriere"]

def getPret(obiect):
    '''
    da pretul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: pretul obiectului
    '''

    return obiect["pret"]


def getLocatie(obiect):
    '''
    da locatia unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: locatia obiectului
    '''

    return obiect["locatie"]

def toString(obiect):

    return "Id: {}, Nume: {}, Descriere : {}, Pret : {}, Locatie : {} ".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )