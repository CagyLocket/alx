import random

los_1 = random.randint(1,10)
los_2 = random.randint(1,10)
wynik_komp = los_1* los_2

wynik = input(f"Ile to jest {los_1} x {los_2}?")

print(f"Odpowiedź użytkownika: {wynik}")
print(f"Odpowiedź komputera: {wynik_komp}")

