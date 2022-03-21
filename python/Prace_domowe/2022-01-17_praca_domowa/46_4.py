# Ex. 46_4

# Wypełnij listę 10-elementową dowolnymi wartościami z zakresu 1-10
# Zaprojektuj algorytm, który wypisze tylko te liczby, które się nie powtarzają
# w liście.
# [2,5,3,6,8,4,1,2,6,5]
# Wypisane zostaną wartości: 3,8,4,1

import random


def unique_nums_generator():

    nums = []
    unique_nums = []
    dict_unique_nums = {}

    for i in range(10):
        num = random.randint(1, 10)
        nums.append(num)

        if num not in dict_unique_nums:
            dict_unique_nums[num] = 1
        else:
            dict_unique_nums[num] += 1

    for j in dict_unique_nums:
        if dict_unique_nums[j] == 1:
            unique_nums.append(j)

    return nums, dict_unique_nums, unique_nums


a, b, c = unique_nums_generator()

# print(a)    # prints out a list with all the numbers
# print(b)    # prints out a dict with pairs of number: its counter
# print(c)    # prints out a list of unique numbers


def print_out():
    print(f"Wylosowane liczby to: {a}")
    print(f"Liczby, które się nie powtarzają to:", end=" ")

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
