# Ex 72

class Auto:

    def __init__(self, marka, model, cena, kolor, silnik):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik

ob1 = Auto("BMW", "X5", 123, "czerwony", "ON")
ob2 = Auto("MB", "GLE", 456, "zielony", "E95")
ob3 = Auto("VW", "Passat", 789, "czarny", "E98")

print(ob1.marka, ob1.model, ob1.cena, ob1.kolor, ob1.silnik)
print(ob2.marka, ob2.model, ob2.cena, ob2.kolor, ob2.silnik)
print(ob3.marka, ob3.model, ob3.cena, ob3.kolor, ob3.silnik)

