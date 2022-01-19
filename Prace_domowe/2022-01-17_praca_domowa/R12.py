# Ex. R12
#
# Utwórz dwuwymiarową listę w układzie 5x5 i wypełnij ją dowolnymi wartościami liczbowymi 1 – 10.
#
# 16892
# 54638
# 32102
# 96236
# 47870
#
# Zaprojektuj kod, który przedstawi wygenerowaną listę w postaci macierzy (jak na powyższym przykładzie)
# Wyznacz dla każdego wiersza i każdej kolumny największą i najmniejszą wartość.

import random

def create_list():

    nums = []

    for i in range(5):
        num = []
        nums.append(num)
        for j in range(5):
            k = random.randint(1, 9)
            num.append(k)

    return nums


a = create_list()

print("--- random 5x5 list ---")
print(a)
print()


def print_matrix(my_list):
    print("--- matrix view of a 5x5 list ---")
    for i in a:
        for j in i:
            print(j, " ", end="")
        print()


print_matrix(a)


def find_max_min_in_rows(a):

    row_max_list = []
    row_min_list = []

    for i in a:
        my_set = set()
        for j in i:
            my_set.add(j)
        # print(my_set)

        max_num = 0
        for k in my_set:
            if (k > max_num):
                max_num = k
        row_max_list.append(max_num)

        min_num = 10
        for k in my_set:
            if (k< min_num):
                min_num = k
        row_min_list.append(min_num)

    return row_max_list, row_min_list


b = find_max_min_in_rows(a)


def convert_columns_to_lists(a):

    col_list = []

    for x in range(5):
        for i in a:
            col_list.append(i[x])
    # print(col_list)  # prints all columns in 1 col list

    # slice the col list to 5 separate lists
    col_list_1 = col_list[:5]
    col_list_2 = col_list[5:10]
    col_list_3 = col_list[10:15]
    col_list_4 = col_list[15:20]
    col_list_5 = col_list[20:]

    # print(col_list_1)
    # print(col_list_2)
    # print(col_list_3)
    # print(col_list_4)
    # print(col_list_5)

    return col_list, col_list_1, col_list_2, col_list_3, col_list_4, col_list_5


c, d, e, f, g, h = convert_columns_to_lists(a)


def find_max_min_in_cols(col_list):

    col_max_list = []
    col_min_list = []

    col_set = set()
    for i in col_list:
        col_set.add(i)

    max_num = 0
    for k in col_set:
        if (k > max_num):
            max_num = k
    col_max_list.append(max_num)

    min_num = 10
    for k in col_set:
        if (k< min_num):
            min_num = k
    col_min_list.append(min_num)

    return col_max_list, col_min_list


j1, j6 = find_max_min_in_cols(d)
j2, j7 = find_max_min_in_cols(e)
j3, j8 = find_max_min_in_cols(f)
j4, j9 = find_max_min_in_cols(g)
j5, j10 = find_max_min_in_cols(h)

print()
print("--- Rows:---")
print(f"Row 1 -> max = {b[0][0]} & Min = {b[1][0]}")
print(f"Row 2 -> max = {b[0][1]} & Min = {b[1][1]}")
print(f"Row 3 -> max = {b[0][2]} & Min = {b[1][2]}")
print(f"Row 4 -> max = {b[0][3]} & Min = {b[1][3]}")
print(f"Row 5 -> max = {b[0][4]} & Min = {b[1][4]}")
print()

print("--- Columns:---")
print(f"Column 1 -> Max = {j1[0]} & Min = {j6[0]}")
print(f"Column 2 -> Max = {j2[0]} & Min = {j7[0]} ")
print(f"Column 3 -> Max = {j3[0]} & Min = {j8[0]} ")
print(f"Column 4 -> Max = {j4[0]} & Min = {j9[0]} ")
print(f"Column 5 -> Max = {j5[0]} & Min = {j10[0]} ")