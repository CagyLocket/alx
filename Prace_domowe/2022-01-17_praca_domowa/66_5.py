# Ex. 66-5

# Utwórz dwie listy 10-cio elementowe z losowymi wartościami 1-20.
# ❑ Każda z list posiada różne wartości.
# ❑ Napisz funkcję, która wypisze największą wartość występującą jednocześnie w obu listach
#
# lista1 = [2,5,8,4,15]
# lista2 = [6,3,2,8,12]
# Największa liczba występująca w obu listach to: 8


import random


def create_2_lists():

    nums_1 = []
    nums_2 = []

    for num in range(10):
        num = random.randint(1, 20)
        nums_1.append(num)

    for num in range(10):
        num = random.randint(1, 20)
        nums_2.append(num)
    return nums_1, nums_2


a, b = create_2_lists()


def find_max_num_in_2_lists(nums_1, nums_2):

    nums_set = {}

    for i in nums_1:
        for j in nums_2:
            if (i == j):
                nums_set[i] = j
    try:
        found = False
        max_num = 0
        msg = ""
        for i in nums_set:
            if (i > max_num):
                found = True
                max_num = i
        if (found == False):
            msg = "Oops... listy nie mają wspólnych liczb."

    except ValueError:
        print("Listy nie mają wspólnych liczb.")

    return max_num, nums_set, msg


c, d, e = find_max_num_in_2_lists(a, b)


def print_out():
    print(f"Lista 1 = {a}")
    print(f"Lista 2 = {b}")
    print(f"Wspólne liczby = {d}")    # prints out a dict with duplicate nums
    print("----")

    if (c):
        print(f"Największa liczba występująca w obu listach to: {c}")
    else:
        print(f"{e}")

print_out()