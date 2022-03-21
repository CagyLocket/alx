# Cwiczenie 37_5 #

# Napisz grę do nauki tabliczki mnożenia.
# ❑ Ten program ma wylosować dwie liczby z zakresu (1-10), po czym zapytać
# użytkownika ile wyjdzie jak się je pomnoży.
# ❑ Użytkownik podaje swój wynik.
# Ile to jest 3 * 7 ?
# Jeżeli użytkownik poda dobry wynik to program poinformuje go, że wynik jest
# poprawny w przeciwnym razie poda że wynik jest błędny.



# Get two random digits & their multiplication
import random
numb_1 = random.randint(1,10)
numb_2 = random.randint(1,10)

q_computer = numb_1 * numb_2
# print(q_computer)

# User to do multiplication and receive a check-up
q_user = int(input(f"Ile to jest {numb_1} * {numb_2} ?"))

if(q_computer == q_user):
    print("Wynik jest poprawny!")
else:
    print("Wynik jest błędny.")
