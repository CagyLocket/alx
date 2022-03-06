# for i in range(0, 100, 10):
#     print("%-5i%-10i%15i" % (i, i**2, i**3))

# s - dla stringa
# i - dla liczby
# %f.4f - po procen cie ile rezerwujemy przestrzeni, .4 jakie zaokrąglenie
# %-4 -> minus wyrównuje do lewej

#
# for i in range(0, 100, 10):
#     print("Pierwiastkiem liczby %2i jest liczba %5.2f" % (i, i**0.5))

for i in range(0, 100, 10):
    print("%05i - %010i - %15i" % (i, i**2, i**3))