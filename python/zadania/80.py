class Produkt:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Oprogramowanie(Produkt):

    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system


class Szkolenia(Oprogramowanie):

    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def __str__(self):
        return (f"{self.nazwa}, {self.cena}, {self.jezyk}, {self.system}, {self.termin}")

k1 = Szkolenia("Szkolenie Python", 100, "Python", "Windows", "2017-06-01")
print(k1)
