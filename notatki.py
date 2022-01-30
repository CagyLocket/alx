
while(True):

    while(True):
        try:
            liczba1 = float(input("Podaj liczba 1:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    while (True):
        try:
            liczba2 = float(input("Podaj liczba 2:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("Nie dzielimy przez zero !")
    except:
        print("Nieoczekiwany blad")
    else:
        print("....")
    finally:
        print("TU BLOK FINALLY")



# Pierwszy kod
while(True):

    while(True):
        try:
            liczba1 = float(input("Podaj liczba 1:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    while (True):
        try:
            liczba2 = float(input("Podaj liczba 2:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("Nie dzielimy przez zero !")
    except:
        print("Nieoczekiwany blad")
    else:
        print("....")
    finally:
        print("TU BLOK FINALLY")

    break


class Bankomat:

    def __init__(self, nazwa, miasto):
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__kasa = 100000000

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def miasto(self):
        return self.__miasto

    @property
    def kasa(self):
        return self.__kasa

    def getNazwa(self):
        return self.__nazwa

    def getMiasto(self):
        return self.__miasto

    def getKasa(self):
        return self.__kasa

    @nazwa.setter
    def nazwa(self, nazwa):
        self.__nazwa = nazwa

    @miasto.setter
    def miasto(self, miasto):
        self.__miasto = miasto

    @kasa.setter
    def kasa(self, kasa):
        self.__kasa = kasa

    def setNazwa(self, nazwa):
        self.__nazwa = nazwa

    def setMiasto(self, miasto):
        self.__miasto = miasto

    def setKasa(self, kasa):
        self.__kasa = kasa

bankomat = Bankomat("Euronet", "Gdańsk")

bankomat.nazwa = "PKOSA"
bankomat.miasto = "Warszawa"
bankomat.kasa = 44444

bankomat.setNazwa("ING")
bankomat.setMiasto("Poznań")
bankomat.setKasa(999909)

print(bankomat.nazwa, bankomat.miasto, bankomat.kasa)
print(bankomat.getNazwa(), bankomat.getMiasto(), bankomat.getKasa())


class Pojazdy:

    def __init__(self, model, cena, kolor):
        self.model = model
        self.cena = cena
        self.kolor = kolor

class Samolot(Pojazdy):

    def __init__(self, model, cena, kolor, pulap):
        super().__init__(model, cena, kolor)
        self.pulap = pulap

    def __str__(self):
        return (f"{self.model} {self.cena} {self.kolor} {self.pulap}")

ob = Samolot("Awionetka", 11111, "biały", 22222)
print(ob)


plik = open("dane.txt", "a")

# plik.write("aaaa111\n")
# plik.write("bbbb222\n")
# plik.write("cccc333\n")

# dane = ["cccc\n", "ggggg\n", "jjjjjj\n"]
# for i in dane:
#     plik.write(i)

dane = ["cccc\n", "ggggg\n", "jjjjjj\n", "oooooo\n", "64253642562\n"]
plik.writelines(dane)


plik.close()