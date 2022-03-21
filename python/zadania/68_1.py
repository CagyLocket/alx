# Ex. 68-1

class Pracownik:

    def __init__(self, imie, nazwisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon


lista_pracownikow = []


while (True):

    menu = input(
        "D-dodaj pracownika, P-pokaz pracownikow, U-usun pracownika, Z-zmien dane pracownikowi, K-koniec: ").upper()

    if (menu == "D"):
        # pytania: imie, nazwisko, telefon, email
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj telefon: ")
        email = input("Podaj email: ")

        pracownik = Pracownik(imie, nazwisko, telefon, email)
        lista_pracownikow.append(pracownik)
        print("Pomyślnie dodano pracownika")



    elif (menu == "P"):
        # prezentacja: Imię:.... Nazwisko:... Telefon:.... Email: ....
        for i in lista_pracownikow:
            print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}, Telefon: {i.telefon}, Email: {i.email}")

    elif (menu == "U"):
        # pytania: nazwisko
        q = input("Podaj nazwisko użytkownika, którego chcesz usunąć: ")

        znaleziono = False
        for i in lista_pracownikow:
            if (q == i.nazwisko):
                znaleziono = True
                lista_pracownikow.remove(i)
                print("Pomyślnie usunięto kontakt.")
                break

        if (znaleziono == False):
            print("Nie znaleziono kontaktu o podanym nazwisku.")
            # pytania: nazwisko


    elif (menu == "Z"):
        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon, nowyEmail
        q = input("Podaj nazwisko użytkownika, którego dane chcesz zmienić: ")

        znaleziono = False
        for i in lista_pracownikow:
            if (q == i.nazwisko):
                znaleziono = True
                nowe_imie = input("Podaj nowe imię: ")
                i.imie = nowe_imie
                nowe_nazwisko = input("Podaj nowe nazwisko: ")
                i.nazwisko = nowe_nazwisko
                nowy_telefon = input("Podaj nowy telefon: ")
                i.telefon = nowy_telefon
                nowy_email = input("Podaj nowy email: ")
                i.email = nowy_email

        if (znaleziono == False):
            print("Nie ma takiego użytkownika w bazie danych.")

    elif (menu == "K"):
        break
    else:
        print("Nierozpoznana opcja menu")