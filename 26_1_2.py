import random

# weź wertość i sprawdź czy jest taka sama jak kolejne
# jak jest to zrób zliczenie wystapień

lista = []
zbior = set()

for i in range(1, 11):
    a = random.randint(1, 10)
    lista.append(a)

zbior.update(lista)

for i in zbior:
    licznik = 0
    for j in lista:
        if (i == j):
            licznik += 1
    print(f"{i} występuje {licznik} razy.")

print(lista)
print(zbior)



