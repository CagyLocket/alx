kontakty = []

while(True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, S-szukaj, K-koniec: ").upper()

    if(menu == "D"):
        # pytania: imie, nazwisko, telefon
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj telefon: ")

        kontakt = [imie, nazwisko, telefon]
        kontakty.append(kontakt)
        print('Pomyslnie dodano kontakt')

    elif(menu == "P"):
        for i in kontakty:
            print(f"Imię: {i[0]}, Nazwisko: {i[1]}, Telefon: {i[2]}")
        # Imię: .... Nazwisko: .... Telefon: ....

    elif (menu == "U"):
        q = input("Podaj nazwisko użytkownika, którego chcesz usunąć: ")

        znaleziono = False
        for i in kontakty:
             if (q == i[1]):
                znaleziono = True
                kontakty.remove(i)
                print("Pomyślnie usunięto kontakt")
                break

        if(znaleziono == False):
            print("Nie znaleziono kontaktu o podanym nazwisku")
            # pytania: nazwisko

    elif (menu == "Z"):
        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon
        q = input("Podaj nazwisko użytkownika, którego dane chcesz zmienić: ")

        znaleziono = False
        for i in kontakty:
            if (q == i[1]):
                znaleziono = True
                nowe_imie = input("Podaj nowe imię: ")
                i[0] = nowe_imie
                nowe_nazwisko = input("Podaj nowe nazwisko: ")
                i[1] = nowe_nazwisko
                nowy_telefon = input("Podaj nowy telefon: ")
                i[2] = nowy_telefon

        if (znaleziono == False):
            print("Nie ma takiego użytkownika w bazie danych.")

    elif (menu == "S"):
        # pytania: podaj fraze szukania (imienie i nazwisku)
        q = input("Podaj imię lub nazwisko użytkownika: ")

        znaleziono = False
        for i in kontakty:
            if (q == i[0] or q == i[1]):
                znaleziono = True
                print(f"Imię: {i[0]}, Nazwisko: {i[1]}, Telefon: {i[2]}")

        if (znaleziono == False):
            print("Nie ma takiego użytkownika w bazie danych.")

    elif (menu == "K"):
        print("koniec programu")
        break
    else:
        print("Nierozpoznana opcja menu")