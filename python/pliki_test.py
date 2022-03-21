plik = open("dane.txt", "r", encoding="utf-8")

# 1 sposob
# print(plik.readline())
# print(plik.readline())
# print(plik.readline())

# 2 sposob
# dane = plik.readlines()
# for i in dane:
#     print(i.strip())

# 3 sposob
for i in plik:
    print(i.strip())

plik.seek(0)

for i in plik:
    print(i.strip())

plik.close()
