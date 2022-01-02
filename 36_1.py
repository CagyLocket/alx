liczby = {1:"jeden", 2: "dwa", 3:"trzy", 4:"cztery"}

liczba_los = input("Podaj liczbę 4-cyfrową:")

a = int(liczba_los[0])
b = int(liczba_los[1])
c = int(liczba_los[2])
d = int(liczba_los[3])

wynik = (liczby[a], liczby[b], liczby[c], liczby[d])
print(wynik)