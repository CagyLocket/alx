# Cwiczenie 46 #

# Zadeklaruj 6 zmiennych i przypisz im dowolne wartości liczbowe (różne).
# Zaimplementuj kod, który wyświetli informację dotycząca minimalnej i maksymalnej wartości tj.:
# a = 5; b = 10; c = 100; d = 1; e = 50; f = 3;
# Min to: 1, Max to: 100
# Zadanie 46 zaprojektujcie w oparciu o poznaną instrukcję warunkową if.
# Mała podpowiedź do zadania 46:
# - w tym zadaniu nie jest wymagane stosowanie ifów ze złożonymi warunkami. Całkowicie wystarczą ify, które będą miały tylko jeden warunek. Tak więc jak ktoś będzie miał pomysł na takiego ifa: if(a>b and a>c and a>d itd...) - to niech tego nie robi :)
# - w tym zadaniu nie jest wymagane stosowanie zagnieżdżeń ifów, czyli ifa w ifie nie trzeba robić.
# - myślę że pomocne będzie utworzenie dodatkowych zmiennych np.: najmniejsza, najwieksza
# - zabronione jest wykorzystywanie list i mechanizmów sortujących.


# Create an empty set for random digits
numb_set = set()

# Declare 6 random variables and add them into the set()
import random
numb_1 = random.randint(1,100)
numb_set.add(numb_1)
numb_2 = random.randint(1,100)
numb_set.add(numb_2)
numb_3 = random.randint(1,100)
numb_set.add(numb_3)
numb_4 = random.randint(1,100)
numb_set.add(numb_4)
numb_5 = random.randint(1,100)
numb_set.add(numb_5)
numb_6 = random.randint(1,100)
numb_set.add(numb_6)

# Create supporting variables
current_min = 0
current_max = 0

# Find max
if(numb_1 > current_max):
    current_max = numb_1

if(numb_2 > current_max):
    current_max = numb_2

if(numb_3 > current_max):
    current_max = numb_3

if(numb_4 > current_max):
    current_max = numb_4

if(numb_5 > current_max):
    current_max = numb_5

if(numb_6 > current_max):
    current_max = numb_6

# Find min
if (numb_1 > current_min):
    current_min = numb_1

if (numb_2 < current_min):
    current_min = numb_2

if (numb_3 < current_min):
    current_min = numb_3

if (numb_4 < current_min):
    current_min = numb_4

if (numb_5 < current_min):
    current_min = numb_5

if (numb_6 < current_min):
    current_min = numb_6

# Outcome
print(f"a = {numb_1}; b = {numb_2}; c = {numb_3}; d = {numb_4}, e = {numb_5}, f = {numb_6}; ")
print(f"Min to: {current_min}")
print(f"Max to: {current_max}")






