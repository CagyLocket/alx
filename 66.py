import random

los = []

for i in range(10):
    a = random.randint(1,100)
    los.append(a)

# print(los)

def licz(dane):
    min = dane[0]
    max = dane[0]
    ile = 0
    ile2 = 0
    avg = 0
    sum =0

    for i in dane:
        if (i < min):
            min = i

        if (i > max):
            max = i

        sum += i
        avg = sum / len(dane)

        if (i % 2 == 0):
            ile += 1

        if (i % 2 != 0):
            ile2 += 1

    return max, min, avg, ile, ile2


licz(los)

print(los)

x = licz(los)
print(f"Największa wartość: {x[0]}")
print(f"Najmniejsza wartość: {x[1]}")
print(f"Średnia: {x[2]}")
print(f"Ilość liczb parzystych: {x[3]}")
print(f"Ilość liczb nieparzystych: {x[4]}")
