ciag_cyfr= input("Wprowadź ciąg znaków: ")

cyfry = {
    0: "zero",
    1: "jeden",
    2: "dwa",
    3: "trzy",
    4: "cztery",
    5: "piec",
}

for x in ciag_cyfr:
    # print(x)
    print(cyfry[int(x)], end=' ')
