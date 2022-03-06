import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


plik = open("72_4.txt", "r", encoding="utf8")
dane_plik = plik.readlines()
plik.close()
# print(dane_plik)

warszawa = 0
szczecin = 0
bydgoszcz = 0

for i in dane_plik:
    dane = i.split(";")
    if dane[2] == "Warszawa\n":
        warszawa += 1
    elif dane[2] == "Szczecin\n":
        szczecin += 1
    elif dane[2] == "Bydgoszcz\n":
        bydgoszcz += 1

ilosc_studentow = []
ilosc_studentow.append(warszawa)
ilosc_studentow.append(szczecin)
ilosc_studentow.append(bydgoszcz)

miasta = ['Warszawa', 'Szczecin', "Bydgoszcz"]

plt.bar(miasta, ilosc_studentow)

plt.show()