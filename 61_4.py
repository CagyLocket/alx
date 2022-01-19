
suma = 0
for i in range(3):
    liczba = int(input(f"Podaj liczbę: "))
    if(liczba%2 == 0):
        suma += liczba

print(suma)