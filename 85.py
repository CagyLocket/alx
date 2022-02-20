


def dodaj(imie, nazwisko, grupa):
    plik = open("85.txt", "a", encoding="utf8")
    plik.write(f"{imie};{nazwisko};{grupa}\n")
    plik.close()
    print("Student dodany pomyślnie.")


def pokaz():
    plik = open("85.txt", "r", encoding="utf8")
    for i in plik:
        dane = i.split(";")
        print(f"Imię: {dane[0]}, Nazwisko: {dane[1]}, Grupa: {dane[2].strip()}")

    plik.close()

def usun(nazwisko):

    # 1 sposób
    plik = open("85.txt", "r", encoding="utf8")
    dane = plik.readlines()
    plik.close()

    for i in dane:
        i_split = i.split(";")
        if i_split[1] == nazwisko:
            dane.remove(i)

    plik = open("85.txt", "w", encoding="utf8")
    plik.writelines(dane)
    plik.close()

    # 2 sposób, czytamy plik i do listy dodajemy tylko te pozycje które chcemy mieć w liście
    # dane = []
    # plik = open("85.txt", "r", encoding="utf8")
    # for i in plik:
    #     i_split = i.split(";")
    #     if i_split[1] != nazwisko:
    #         dane.append(i)
    # plik.close()
    #
    # plik = open("85.txt", "w", encoding="utf8")
    # plik.writelines(dane)
    # plik.close()


def zmien(nazwisko, nowe_imie, nowe_nazwisko):
    plik = open("85.txt", "r", encoding="utf8")
    dane = plik.readlines()
    plik.close()

    for i, x in enumerate(dane):
        x_split = x.split(";")
        if x_split[1] == nazwisko:    

            if nowe_imie != "":
                x_split[0] = nowe_imie

            if nowe_nazwisko != "":
                x_split[1] = nowe_nazwisko

            dane[i] = f"{x_split[0]}; {x_split[1]}; {x_split[2]}"

            plik = open("85.txt", "w", encoding="utf8")
            plik.writelines(dane)
            plik.close()


while (True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-koniec").upper()

    if (menu == "D"):
        # inputy: imie, nazwisko, grupa
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        grupa = input("Podaj nazwę grupy: ")

        dodaj(imie, nazwisko, grupa)

    elif (menu == "P"):
        pokaz()
    elif (menu == "U"):
        # inputy: nazwisko
        nazwisko = input("Podaj nazwisko: ")
        usun(nazwisko)

    elif (menu == "Z"):
        # inputy: nazwisko, noweImie, noweNazwisko
        nazwisko = input('Podaj nazwisko: ')
        nowe_imie = input("Podaj nowe imię: ")
        nowe_nazwisko = input("Podaj nowe nazwisko: ")
        zmien(nazwisko, nowe_imie, nowe_nazwisko)

    elif (menu == "K"):
        break
    else:
        print("nierozpoznana opcja menu")