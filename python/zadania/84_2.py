plik = open("84_2_ksiazki.txt", "r", encoding="utf-8")

for i in plik:
    dane = i.split(";")
    print(f"Autor: {dane[0]}, Tytuł książki: {dane[1]}, Rok wydania: {dane[2]}")

plik.close()