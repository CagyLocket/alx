# Ex. 26_11
#
# Utwórz pustą listę.
# ❑ Zapełnij je pętlą 10-cio losowo wybranymi liczbami z zakresu 1 – 10.
# ❑ Napisz algorytm, który znajdzie i wypisze duplikaty

import random


def duplicate_nums_generator():

    nums = []
    duplicate_nums = []
    dict_duplicate_nums = {}

    for i in range(10):
        num = random.randint(1, 10)
        nums.append(num)

        if num not in dict_duplicate_nums:
            dict_duplicate_nums[num] = 1
        else:
            dict_duplicate_nums[num] += 1

    for j in dict_duplicate_nums:
        if dict_duplicate_nums[j] != 1:
            duplicate_nums.append(j)

    return nums, dict_duplicate_nums, duplicate_nums


a, b, c = duplicate_nums_generator()

# print(a)    # prints out a list with all the numbers
# print(b)    # prints out a dict with pairs of number: its counter
# print(c)    # prints out a list of duplicate numbers


def print_out():
    print(f"Wylosowane liczby to: {a}")
    print(f"Liczby, które się powtarzają to:", end=" ")

    try:
        print(f"{c[0]}, ", end=" ")
        print(f"{c[1]}, ", end=" ")
        print(f"{c[2]}, ", end=" ")
        print(f"{c[3]}, ", end=" ")
        print(f"{c[4]}, ", end=" ")
        print(f"{c[5]}, ", end=" ")
        print(f"{c[6]}, ", end=" ")
        print(f"{c[7]}, ", end=" ")
        print(f"{c[8]}, ", end=" ")
        print(f"{c[9]} ", end=" ")

    except IndexError:
        pass

print_out()
