# Ex. 59-1
#
# ❑ Zaprojektuj program, który będzie losował liczby (1-10) wraz z działaniem (dodawanie, odejmowanie i mnożenie)
# i pytał użytkownika jaki jest to wynik np.:
#
# Ile to jest: 2 * 2 ?
# Ile to jest: 9 – 4 ?
# Ile to jest: 3 * 9 ?
# ...
#
# ❑ Takich pytań powinno być 10.
# ❑ Program po 10 pytaniach prezentuje statystyki odpowiedzi
# to znaczy na ile pytań odpowiedziano poprawnie, a na ile błędnie.


import random


def multiplication_results():

    results = {
        0: 0,   # False
        1: 0    # True
    }

    # number of questions to a user
    q_num = 10

    for i in range(1, q_num+1):
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)

        op = {
            1: "+",
            2: "-",
            3: "*"
        }
        rand_op = op[random.randint(1, 3)]
        # print(rand_op)

        print(f"Pytanie nr {i} z {q_num}: Ile to jest {num_1} {rand_op} {num_2}?")

        if (rand_op == op[1]):
            comp_result = num_1 + num_2
        elif (rand_op == op[2]):
            comp_result = num_1 - num_2
        else:
            comp_result = num_1 * num_2
        # print(comp_result)

        while(True):
            try:
                user_result = int(input("Twoja odpowiedź:"))
            except ValueError:
                print(f"Ile to jest {num_1} {rand_op} {num_2}?")
                continue
            break

        if (user_result == comp_result):
            print(f"Poprawny wynik :)")
            results[1] += 1
        else:
            results[0] += 1
            print(f"Niepoprawny wynik :(")
            continue

    # choose a form of a word "pytanie" in print statements
    q_false = ""  # for results False
    if (results[0] == 0 or results[0] >= 5):
        q_false = "pytań"
    if (results[0] == 1):
        q_false = "pytanie"
    if (results[0] >= 2 and results[0] < 5):
        q_false = "pytania"

    # choose a form of a word "pytanie" in print statements
    q_true = ""  # for results True
    if (results[1] == 0 or results[1] >= 5):
        q_true = "pytań"
    if (results[1] == 1):
        q_true = "pytanie"
    if (results[1] >= 2 and results[1] < 5):
        q_true = "pytania"

    print()
    print("--- Podsumowanie ---")
    print(f"Poprawnie odpowiedziano na: {results[1]} {q_true}.")
    print(f"Błędnie odpowiedziano na: {results[0]} {q_false}.")
    # print(results)


multiplication_results()







































