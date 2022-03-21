# mechanizm obliczania potęgi bez użycia operatora **

podstawa = int(input("Podaj podstawę: "))
wykladnik = int(input("Podaj wykładnik: "))
if(wykladnik < 0):
    print("Wykładnikiem potęgi musi być liczba większa lub równa 0")
else:
    wynik = 1
    for i in range(wykladnik):
        wynik = wynik * podstawa

print(wynik)
