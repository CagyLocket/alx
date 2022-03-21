class Pracownik:

    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__kontrakt = kontrakt
        self.__pensja = pensja

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def kontrakt(self):
        return self.__kontrakt

    @property
    def pensja(self):
        return self.__pensja


    @imie.setter
    def imie(self, imie):
        self.__imie = imie

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    @kontrakt.setter
    def kontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    @pensja.setter
    def pensja(self, pensja):
        self.__pensja = pensja

    def __str__(self):
        return (f"imię: {self.imie}, nazwisko: {self.nazwisko}, kontrakt: {self.kontrakt}, pensja: {self.pensja} ")



class PracownikController:

    def __init__(self):
        self.lista_pracownikow = []

    def dodaj_pracownika(self, imie, nazwisko, kontrakt, pensja):
        pracownik = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.lista_pracownikow.append(pracownik)
        print("Dane zostały pomyślnie dodane.")

    def pokaz_pracownikow(self):
        for i in self.lista_pracownikow:
            print(f"Imię: {i.imie}, Nazwisko: {i.nazwisko}, Kontrakt: {i.kontrakt}, Pensja: {i.pensja}")

    def usun_pracownika(self, nazwisko):

        znaleziono = False
        for i in self.lista_pracownikow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                self.lista_pracownikow.remove(i)
                print("Pomyślnie usunięto pracownika.")
                break

        if znaleziono == False:
            print("Nie znaleziono pracownika o podanym nazwisku.")


    def is_etat(self, nazwisko):
        for i in self.lista_pracownikow:
            if nazwisko == i.nazwisko:
                if i.kontrakt == "etat":
                   return True
                else:
                    return False
            # else:
            #     print("Nie ma takiego pracownika.")

    def zmien_kontrakt_pracownikowi(self, nazwisko, nowa_pensja):

        znaleziono = False
        for i in self.lista_pracownikow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                i.pensja = nowa_pensja
                print("Pomyślnie zmieniono kontrakt pracownikowi (1).")
                break

        if znaleziono == False:
            print("Nie znaleziono pracownika o podanym nazwisku (2).")

    def zmien_kontrakt_pracownikowi_staz(self, nazwisko, nowy_kontrakt, nowa_pensja):

        znaleziono = False
        for i in self.lista_pracownikow:
            if (nazwisko == i.nazwisko):
                znaleziono = True
                i.pensja = nowa_pensja
                i.kontrakt = nowy_kontrakt
                print("Pomyślnie zmieniono kontrakt pracownikowi (3).")
                break

        if znaleziono == False:
            print("Nie znaleziono pracownika o podanym nazwisku (4).")


class Firma(PracownikController):

    def __init__(self, nazwa_firmy):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.menu()

    def menu(self):

        while (True):

            menu = input(
                f"Witaj w firmie: {self.nazwa_firmy}\nD-dodaj, P-pokaz, U-usun, Z-zmien kontrakt, K-koniec").upper()

            if (menu == "D"):
                imie = input("Podaj imię pracownika: ")
                nazwisko = input("Podaj nazwisko pracownika: ")
                kontrakt = input("Jaki kontrakt: S-staz, E-etat").upper()

                if(kontrakt == "S"):
                    kontrakt = "staż"
                    self.dodaj_pracownika(imie, nazwisko, kontrakt, 1000)

                elif(kontrakt == "E"):
                    kontrakt = "etat"
                    pensja = int(input("Podaj pensje pracownika"))
                    self.dodaj_pracownika(imie, nazwisko, kontrakt, pensja)
                else:
                    print("Wybrano niepoprawny kontrakt")

            elif (menu == "P"):
                # imie, nazwisko, kontrakt, pensja - PETLA
                self.pokaz_pracownikow()

            elif (menu == "U"):
                # pytania: nazwisko
                nazwisko = input("Podaj nazwisko pracownika: ")
                self.usun_pracownika(nazwisko)

            elif (menu == "Z"):
                # pytania: nazwisko, pensja
                nazwisko = input("Podaj nazwisko pracownika: ")
                self.is_etat(nazwisko)

                if self.is_etat(nazwisko):
                    nowa_pensja = int(input("Podaj nowe pensję: "))
                    self.zmien_kontrakt_pracownikowi(nazwisko, nowa_pensja)

                else:
                    nowy_kontrakt = "etat"
                    nowa_pensja = int(input("Podaj nowe pensję: "))
                    self.zmien_kontrakt_pracownikowi_staz(nazwisko, nowy_kontrakt, nowa_pensja)

            elif (menu == "K"):
                break

firma = Firma("Python Sp z o.o.")



