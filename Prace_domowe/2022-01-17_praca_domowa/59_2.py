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
# ❑ Kiedy użytkownik odpowie poprawnie, otrzymuje kolejne pytanie.
# ❑ Kiedy użytkownik odpowie źle program pyta ponownie o to samo.

import random


def multiplication_results():

    for i in range(1, 20):
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        print(f"Pytanie nr {i}: Ile to jest {num_1} * {num_2}?")
        comp_result = num_1 * num_2
        try:
            user_result = int(input("Twoja odpowiedź:"))
        except ValueError:
            print("Podawaj tylko liczby całkowite.")

        while(True):

                if (user_result == comp_result):
                    print(f"Wynik poprawny")
                    break

                else:
                    print(f"Niepoprawny wynik :(")
                    print(f"Ile to jest {num_1} * {num_2}?")
                    try:
                        user_result = int(input("Twoja odpowiedź:"))
                    except ValueError:
                        print("Podawaj tylko liczby całkowite.")

        # break


multiplication_results()