plik = open("84_1_imiona.txt", "r", encoding="utf-8")

num = 0
for i in plik:
    num +=1
    print(f"Imię ({num}): {i.strip()}")