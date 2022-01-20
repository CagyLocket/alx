# Ex. 59-2
#
# ❑ Zaprojektuj program, który będzie losował liczby (1-10) pytał użytkownika jaki jest wynik mnożenia np.:
#
# Ile to jest: 2 * 2 ?
# Ile to jest: 9 * 4 ?
# Ile to jest: 3 * 9 ?
# ...
#
# ❑ Pytań powinno być 5.

import random


def multiplication_results():

    for i in range(5):
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        # print(num_1 * num_2)

        print(f"Ile to jest: {num_1} * {num_2}?")
        try:
            user_result = int(input("Twoja odpowiedź:"))
        except ValueError:
            print("Podawaj tylko liczby całkowite.")
            print()
            continue

        comp_result = num_1 * num_2
        if (user_result == comp_result):
            print(f"Wynik poprawny")
        else:
            print(f"Ooops... :(")
            print(f"Poprawna odpowiedź to: {comp_result}")
            print()
            continue


multiplication_results()