# Krok 1
lista = []
liczba_1 = int(input("Podaj liczbę całkowitą:"))
lista.append(liczba_1)
liczba_2 = int(input("Podaj liczbę całkowitą:"))
lista.append(liczba_2)
liczba_3 = int(input("Podaj liczbę całkowitą:"))
lista.append(liczba_3)
liczba_4 = int(input("Podaj liczbę całkowitą:"))
lista.append(liczba_4)
liczba_5 = int(input("Podaj liczbę całkowitą:"))
lista.append(liczba_5)


#print(lista)

# Krok 2
print(lista)
suma = lista[0]+lista[1]+lista[2]+lista[3]+lista[4]
print(f"Suma wszystkich liczb w liście wynosi {suma}")
srednia = suma / len(lista)
print(f"Średnia wszystkich liczb w liście wynosi {srednia}")
