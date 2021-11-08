from DomainLab567.obiect import getNume, getId, getLocatie, getPret, getDescriere, creeazaObiect


def mutareObiect(locatia1, locatia2, lista):
    '''
    mutarea tuturor obiectelor dintr-o locatie in alta
    :param locatia1: string
    :param locatia2: string
    :param lista: lista de obiecte
    :return: lista in care obiectele au fost mutate
    '''

    listaNoua=[]
    for obiect in lista:
        if getLocatie(obiect)==locatia1:
            obiectNou=creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect),
                getPret(obiect),
                locatia2
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua

def concatenareString(string, valoare, lista):
    '''
    concateneaza un string la toate descrierile obiectelor cu pretul mai mare decât valoarea data
    :param string: string
    :param valoare: float
    :param lista: lista de obiecte
    :return: lista dupa ce s-a efectuat concatenarea
    '''

    listaNoua = []
    for obiect in lista:
        pret = getPret(obiect)
        if pret > valoare:
            obiectNou = creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect) + " " + string,
                getPret(obiect),
                getLocatie(obiect)
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
