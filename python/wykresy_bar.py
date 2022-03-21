import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

dane = [10, 120, 30, 140, 44]
info = ['Google', 'Facebook', "app", 'Onet', 'Yahoo']

plt.bar(info, dane)

plt.show()