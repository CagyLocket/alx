
class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodaj_ocena(self, ocena):
        self.oceny.append(ocena)

    def wypisz_oceny(self):
        for z in self.oceny:
            print(f"Twoje oceny to: {z}")

    def policz_srednia(self):
        suma = 0
        for k in self.oceny:
            suma += k

        srednia = suma / len(self.oceny)
        print(srednia)


lista_studentow = []


while(True):

    menu = input("D-dodaj studenta, P-pokaz studentow, U-usun studenta, "
                 "O-dodaj ocenę studentowi, W-wypisz oceny studenta,"
                 "S-srednia studenta, K-koniec").upper()

    if(menu == "D"):
        # pytania: imie, nazwisko
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        student = Student(imie, nazwisko)
        lista_studentow.append(student)

    elif (menu == "P"):
        # prezentacja: Imie:... Nawisko:...
        for i in lista_studentow:
            print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}")

    elif (menu == "U"):
        # pytania: nazwisko
        q = input("Podaj nazwisko studenta: ")

        znaleziono = False
        for i in lista_studentow:
            if (q == i.nazwisko):
                znaleziono = True
                lista_studentow.remove(i)
                print("Pomyślnie usunięto studenta.")
                break

        if (znaleziono == False):
            print("Nie znaleziono studenta o podanym nazwisku.")

    elif (menu == "O"):
        # pytania: nazwisko, ocena
        nazwisko = input("Podaj nazwisko: ")
        ocena = int(input("Dodaj ocenę: "))

        znaleziono = False
        for i in lista_studentow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                i.dodaj_ocena(ocena)
                # i.oceny.append(ocena)
                print("Pomyślnie dodano ocenę.")
                break

        if (znaleziono == False):
            print("Nie znaleziono studenta o podanym nazwisku.")

    elif (menu == "W"):
        # pytania: nazwisko
        nazwisko = input("Podaj nazwisko: ")

        znaleziono = False
        for i in lista_studentow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                i.wypisz_oceny()
                # for j in i.oceny:
                #     print(f"{j}")
                break

        if (znaleziono == False):
            print("Nie znaleziono studenta o podanym nazwisku.")

    elif (menu == "S"):
        # pytania: nazwisko
        nazwisko = input("Podaj nazwisko: ")

        znaleziono = False
        for i in lista_studentow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                i.policz_srednia()
                break

        if (znaleziono == False):
            print("Nie znaleziono studenta o podanym nazwisku.")



    elif (menu == "K"):
        pass