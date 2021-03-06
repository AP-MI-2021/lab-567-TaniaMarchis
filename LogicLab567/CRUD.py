from DomainLab567.obiect import creeazaObiect, getId, getPret

def adaugaObiect(id,nume,descriere,pret,locatie,lista):
    '''
    adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand atat elementele vechi, cat si noul obiect
    '''

    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv!")

    obiect = creeazaObiect(id,nume,descriere,pret,locatie)
    return lista + [obiect]

def getById(id,lista):
    '''
    gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None, daca acesta nu exista
    '''

    for obiect in lista:
        if getId(obiect)==id:
            return obiect
    return None

def stergeObiect(id,lista):
    """
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara elementul cu id-ul dat
    """

    if getById(id, lista) is None:
        raise ValueError("Nu exista un obiect cu id-ul dat!")
    return [obiect for obiect in lista if getId(obiect)!=id]

def modificaObiect(id,nume,descriere,pret,locatie,lista):
    """
    modifica un obiect cu id-ul dat
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: lista modificata
    """

    if getById(id, lista) is None:
        raise ValueError("Nu exista un obiect cu id-ul dat!")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv!")
    listaNoua=[]
    for obiect in lista:
        if getId(obiect)==id:
            obiectNou=creeazaObiect(id,nume,descriere,pret,locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua