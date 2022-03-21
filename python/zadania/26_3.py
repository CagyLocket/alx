
import random

class Sejf:

    def __init__(self):
        self.__tajna_liczba = random.randint(1, 100)

    def odczyt(self, kod):
        if (kod == 1234):
            print(f"Tajna liczba to: {self.__tajna_liczba}")

moj_sejf = Sejf()
moj_sejf.odczyt(1234)