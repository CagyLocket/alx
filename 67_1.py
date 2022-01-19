
while(True):

    list = []

    while(True):
        try:
            num_1 = int(input("Wprowadź liczbę całkowitą: "))
            list.append(num_1)
        except ValueError:
            print("Wprowadzamy tylko liczby całkowite !!")
        else:
            break

    while (True):
        try:
            num_2 = float(input("Wprowadź liczbę rzeczywistą: "))
            list.append(num_2)
        except ValueError:
            print("Wprowadzamy tylko liczby rzeczywiste !!")
        else:
            break

    # print(list)

    while (True):
        try:
            indeks = int((input("Który indeks mam odczytać? ")))
            if (indeks == 0):
                a = list[0]
            elif (indeks == 1):
                a = list[1]
        except ValueError:
            print("Wprowadzamy tylko liczby całkowite !!")
        else:
            break

    print(a)


#### Dokończyć w domu