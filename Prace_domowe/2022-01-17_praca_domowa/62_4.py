# Ex. 62-4
#
# ❑ Napisz program, który pobiera od użytkownika dowolną ilość liczb całkowitych i dodaje je do listy.
# ❑ Jeżeli użytkownik poda – 0 (zero) oznacza to, że więcej liczb użytkownik nie będzie podawał.
# Zera nie dodajemy do listy.
# ❑ Zaprojektuj własny algorytm sortujący, który posortuje rosnąco utworzoną listę i wynik wypisze do konsoli.


def get_numbers():
    nums = []
    while(True):
        try:
            num = int(input("Wpisz liczbę całkowitą, którą chcesz dodać do listy: "))
        except ValueError:
            print("Tylko liczby całkowite!")

        if (num == 0):
            break
        else:
            nums.append(num)

    return nums


a = get_numbers()
print(f"Twoja lista: {a}")


# Selection sort algorithm
def sort_nums(nums):

    for i in range(len(nums)):
        min_num = i
        for j in range(i + 1, len(nums)):
            if (nums[j] < nums[min_num]):
                min_num = j
        nums[i], nums[min_num] = nums[min_num], nums[i]
    sorted_nums = nums

    return sorted_nums


b = sort_nums(a)
print(f'Uporządkowana rosnąco lista: {b}')

