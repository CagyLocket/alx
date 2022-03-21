import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

dane = [10, 2, 3, 4, 23, 43, 65, 4, 34, 76, 43, 34, 767, 87, 23, 45, 56]
dane2 = [120, 5, 6, 44, 23, 43, 365, 4, 34, 76, 445, 44, 767, 5, 24, 75, 56]
plt.plot(dane, label="Dane testowe 1")
plt.plot(dane2, label="Dane testowe 2")

#linie siatki
plt.grid(color='lightblue', linestyle='-.', linewidth=0.6)

plt.legend()

#zapis wykresu
# plt.savefig('wykresy.png', dpi=300)

plt.show()
