from LogicLab567.CRUD import adaugaObiect, stergeObiect, modificaObiect
from UILab567.console import showAll


def comenzi(lista):

    while True:
        try:
            comanda = input("Dati comanda: ")
            if comanda == "help":
                print("Pentru a adauga un nou obiect folositi comanda add, iar apoi introduceti datele separate prin virgula")
                print("Exemplu: add,1,telefon,iphone,2000,cluj")
                print("Pentru a sterge un obiect folositi comanda delete si introduceti id-ul acestuia separat prin virgula")
                print("Exemplu: delete,1")
                print("Pentru a modifica un obiect folositi comanda update si scrieti id-ul acestuia, urmat de noile date, separate prin virgula")
                print("Exemplu: update,1,laptop,asus,3000,iasi")
                print("Pentru a vedea toate obiectele folositi comanda showall")
                print("Pentru a iesi folositi comanda stop")
                print("Puteti folosi mai multe comenzi separandu-le prin ;")
                print("Exemplu: delete,1;showall")
            elif comanda == "stop":
                break
            else:
                comenzi = comanda.split(";")
                for i in range(len(comenzi)):
                    comanda_separata = comenzi[i].split(",")

                    if comanda_separata[0] == "add":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti 5 date! Reincercati!")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        locatie = comanda_separata[5]

                        lista = adaugaObiect(id, nume, descriere, pret, locatie, lista)

                    elif comanda_separata[0] == "delete":
                        if len(comanda_separata) != 2:
                            raise ValueError("Trebuie sa introduceti id-ul obiectului!")
                        id = comanda_separata[1]

                        lista = stergeObiect(id, lista)

                    elif comanda_separata[0] == "update":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti 5 date! Reincercati!")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = comanda_separata[4]
                        locatie = comanda_separata[5]

                        lista = modificaObiect(id, nume, descriere, pret, locatie, lista)

                    elif comanda_separata[0] == "showall":
                        showAll(lista)

                    else:
                        print("Comanda gresita! Reincercati!")

        except ValueError as ve:
            print("Eroare: {} ". format(ve))





