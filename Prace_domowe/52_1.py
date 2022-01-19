liczba = int(input("Podaj liczbę: "))

wynik = 1
for i in range(1, liczba+1):
    # print(i)
    wynik = wynik * i

print(wynik)
