from LogicLab567.CRUD import adaugaObiect
from TestsLab567.TestAll import runAllTests
from UILab567.comenzi import comenzi
from UILab567.console import runMenu


def main():

    runAllTests()
    lista = []
    while True:
        print("Tastati 1 pentru meniu.")
        print("Tastati 2 pentru comenzi.")
        optiune = input()
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            lista = comenzi(lista)




main()