import pickle


class ContactList:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []
        self.email = []


class ContactListController:

    def __init__(self):
        self.kontakty = []

    def dodaj_kontakt(self, imie, nazwisko):
        kontakt = ContactList(imie, nazwisko)
        self.kontakty.append(kontakt)
        self.zapisz_do_pliku()

    def pokaz_kontakty(self):
        for i in self.kontakty:
            print(f"Imię: {i.imie} Nazwisko: {i.nazwisko}")
            for j in i.telefony:
                print(f"Nr telefonu: {j}")
            for k in i.email:
                print(f"Email: {k}")

    def usun_kontakt(self, nazwisko):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                self.kontakty.remove(i)
                self.zapisz_do_pliku()

            else:
                print("Brak nazwiska w kontaktach.")


    def dodaj_telefon(self, nazwisko, telefon):

        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.append(telefon)
                self.zapisz_do_pliku()
                break

            else:
                print("Brak nazwiska w kontaktach.")
                break

    def usun_telefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.telefony.remove(telefon)
                self.zapisz_do_pliku()
                break

            else:
                print("Brak nazwiska w kontaktach.")
                break

    def dodaj_email(self, nazwisko, email):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.email.append(email)
                self.zapisz_do_pliku()
                break

            else:
                print("Brak nazwiska w kontaktach.")
                break

    def usun_email(self, nazwisko, email):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.email.remove(email)
                self.zapisz_do_pliku()
                break

            else:
                print("Brak nazwiska w kontaktach.")
                break

    def zapisz_do_pliku(self):
        plik = open ("86_3.dat", "wb")
        pickle.dump([], plik)
        plik.close()

    def is_found(self, nazwisko):
        is_found = False
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                is_found = True
                break
            else:
                is_found = False
        return is_found


class App(ContactListController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("86_3.dat", "rb")
            self.kontakty = pickle.load(plik)

        except:
            plik = open("86_3.dat", "wb")
            pickle.dump([], plik)

        finally:
            plik.close()

        self.menu()

    def menu(self):

        while (True):
            menu = input("1-dodaj kontakt, 2-pokaz kontakty, 3-usun kontakt, 4-dodaj telefon, 5-usun telefon, "
                         "6-dodaj email, 7-usun email, 8-koniec")

            if (menu == "1"):
                # inputy: imie, nazwisko
                imie = input("Podaj imię: ")
                nazwisko = input("Podaj nazwisko: ")
                self.dodaj_kontakt(imie, nazwisko)

            elif (menu == "2"):
                self.pokaz_kontakty()

            elif (menu == "3"):
                # inputy: nazwisko
                nazwisko = input("Podaj nazwisko: ")
                self.usun_kontakt(nazwisko)

            elif (menu == "4"):
                # inputy: nazwisko, telefon
                nazwisko = input("Podaj nazwisko: ")
                telefon = input("Podaj nr telefonu: ")
                self.dodaj_telefon(nazwisko, telefon)

            elif (menu == "5"):
                # inputy: nazwisko, telefon
                nazwisko = input("Podaj nazwisko: ")
                telefon = input("Podaj nr telefonu: ")
                self.usun_telefon(nazwisko, telefon)

            elif (menu == "6"):
                # inputy: nazwisko, mail
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                self.dodaj_email(nazwisko, email)

            elif (menu == "7"):
                # inputy: nazwisko, mail
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                self.usun_email(nazwisko, email)

            elif (menu == "8"):
                break
            else:
                print("Nierozpoznana opcja menu")


app = App()




