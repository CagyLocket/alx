
class Zawodnik:

    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def calc_bmi(self):
        bmi = round(self.waga / self.wzrost**2, 2)
        print(f"BMI {self.imie} to: {bmi}")


zawodnik_1 = Zawodnik("A", 1.75, 200)
zawodnik_2 = Zawodnik("B", 1.85, 80)

zawodnik_1.calc_bmi()
zawodnik_2.calc_bmi()
