# Ex. 68-2

class Kursant:

    def __init__(self, imie, nazwisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email


class Kurs:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self. miasto = miasto
        self.lista_kursantow = []


lista_kursow = []

while(True):

    menu = input("1-dodaj kurs, 2-wypisz kursy, 3-usun kurs, 4-dodaj kursanta do kursu, 5-wypisz kursantow danego kursu, 6-usun kursanta z kursu, 7-koniec").upper()

    if (menu == "1"):
        # pytania: nazwa, miasto
        nazwa = input("Podaj nazwę: ")
        miasto = input("Podaj miasto: ")

        kurs = Kurs(nazwa, miasto)
        lista_kursow.append(kurs)
        print("Pomyślnie dodano kurs")

    elif (menu == "2"):
        # prezentacja: Nazwa:... Miasto: .....
        for i in lista_kursow:
            print(f"Nazwa: {i.nazwa}, Miasto: {i.miasto}")

    elif (menu == "3"):
        # pytania: nazwa kursu
        q = input("Podaj nazwę kursu, który chcesz usunąć: ")

        znaleziono = False
        for i in lista_kursow:
            if (q == i.nazwa):
                znaleziono = True
                lista_kursow.remove(i)
                print("Pomyślnie usunięto kurs.")
                break

        if (znaleziono == False):
            print("Nie znaleziono kursu o podanej nazwie.")

    elif (menu == "4"):
        # pytania: nazwa kursu, imie, nazwisko, email
        nazwa = input("Podaje nazwę kursu: ")

        for i in lista_kursow:
            if (nazwa == i.nazwa):
                imie = input("Podaj imię: ")
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email")
                kursant = Kursant(imie, nazwisko, email)
                i.lista_kursantow.append(kursant)

    elif (menu == "5"):
        # pytania: nazwa kursu
        nazwa = input("Podaj nazwę kursu, dla którego chcesz wypisać kursantów: ")

        znaleziono = False
        for i in lista_kursow:
            if (nazwa == i.nazwa):
                znaleziono = True
                for j in i.lista_kursantow:
                    print(f"Imię: {j.imie}, Nazwisko: {j.nazwisko}")

        if (znaleziono == False):
            print("Nie znaleziono kursu o takiej nazwie.")

    elif (menu == "6"):
        # pytania: nazwa kursu, nazwisko kursanta
        nazwa = input("Podaj nazwę kursu, dla którego chcesz usunąc kursanta: ")

        znaleziono = False
        for i in lista_kursow:
            if (nazwa == i.nazwa):
                znaleziono = True
                nazwisko = input("Podaj nazwisko kursanta, którego chcesz usunąć: ")
                for j in i.lista_kursantow:
                    if (nazwisko == j.nazwisko):
                        i.lista_kursantow.remove(j)
                        print("Pomyślnie usunięto kursanta.")

        if (znaleziono == False):
            print("Nie znaleziono kursu o takiej nazwie.")

    elif (menu == "7"):
        break