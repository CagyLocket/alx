
class Koszyk:

    def __init__(self):
        self.zakupy = {}


    def dodaj_produkt(self, produkt, ilosc):
        if produkt in self.zakupy:
            self.zakupy[produkt] += ilosc
        else:
            self.zakupy[produkt] = ilosc


    def usun_produkt(self, produkt, ilosc):

        if produkt in self.zakupy:
            if self.zakupy[produkt] > ilosc:
                self.zakupy[produkt] -= ilosc
            elif self.zakupy[produkt] == ilosc:
                self.zakupy.pop(produkt)
            elif self.zakupy[produkt] < ilosc:
                print(f"Nieprawidłowa ilość. W koszyku jest {self.zakupy[produkt]} {produkt}.")
        else:
            print("Nie znaleziono takiego produktu w koszyku.")


sklep = {"sok": 2.50, "woda": 3.55, "cola": 6.25}
koszyk = Koszyk()

while(True):

    menu = input("D-dodaj produkt, P-pokaz zawartość koszyka, U-usun produkt, K-kasa/Koniec").upper()

    if(menu == "D"):
        # pytania: produkt, ilosc
        # o ilosc pytamy jezeli produkt jest w sklepie
        produkt = input("Podaj produkt: ")
        if produkt in sklep:
            ilosc = int(input("Podaj ilość: "))
            koszyk.dodaj_produkt(produkt, ilosc)
        print("Pomyślnie dodano produkt do koszyka.")

    elif (menu == "P"):
        # prezentacja: Produkt:.... Ilosc: .....
        for produkt in koszyk.zakupy:
            print(f"Produkt: {produkt} ilość: {koszyk.zakupy[produkt]}")

    elif (menu == "U"):
        # pytania: produkt, ilosc
        produkt = input("Podaj produkt, który chcesz usunąć z koszyka: ")
        if produkt in sklep:
            ilosc = int(input("Podaj ilość, którą chcesz usunąć: "))
            koszyk.usun_produkt(produkt, ilosc)
            print(f"Pomyślnie usunięto {ilosc} {produkt} z koszyka.")
        else:
            print("Nie ma takiego produktu w koszyku")


    elif (menu == "K"):
        # PARAGON
        # Produkt:.... Ilosc:.... Cena:.... Wartosc:....
        # Produkt:.... Ilosc:.... Cena:.... Wartosc:....
        # Produkt:.... Ilosc:.... Cena:.... Wartosc:....
        # Razem do zaplaty: .... PLN
        print("PARAGON:")
        suma = 0
        for produkt in koszyk.zakupy:
            wartosc = koszyk.zakupy[produkt] * sklep[produkt]
            print(f"Produkt: {produkt} Ilość: {koszyk.zakupy[produkt]} Wartość: {wartosc}")
            suma += wartosc
        print(f"Razem do zapłaty: {suma} PLN")
        break
    else:
        print("Nierozpoznana opcja menu")