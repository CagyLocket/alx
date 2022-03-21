liczba_1 = int(input("Podaj liczbę:"))
liczba_2 = int(input("Podaj liczbę:"))
liczba_3 = int(input("Podaj liczbę:"))

if(liczba_1 > liczba_2 and liczba_1 > liczba_3):
    print(liczba_1)
elif(liczba_2 > liczba_1 and liczba_2 > liczba_3):
    print(liczba_2)
elif (liczba_3 > liczba_1 and liczba_3 > liczba_2):
    print(liczba_3)
else:
    print("liczby są równe")