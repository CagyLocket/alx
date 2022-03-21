import random

lista_1 = []
lista_2 = []
zbior = set()

for i in range(1, 11):
    a = random.randint(1, 51)
    b = random.randint(1, 51)
    # print(i, a, b)
    lista_1.append(a)
    lista_2.append(b)

for i in lista_1:
    for j in lista_2:
        if (i == j):
            zbior.add(i)
            break


print(lista_1)
print(lista_2)
print(zbior)

