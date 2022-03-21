
slownik = {"jeden": 1, "dwa": 2, "trzy": 3, "cztery":4, "pięć": 5}

liczba_1 = input("Podaj liczbę:")
liczba_2 = input("Podaj liczbę:")

suma = slownik[liczba_1] + slownik[liczba_2]
print(suma)




# sklep = {"woda":2.20, "sok":3.33, "cola":5.55}
# sklep = {}
#
# print(sklep)
# # dodajemy
# sklep["woda"] = 2.20
# sklep["cola"] = 3.20
# sklep["chleb"] = 4.20
# print(sklep)
#
# # sprawdzanie - dotyczy kluczy
# print("chleb" in sklep)
#
# # usuwanie
# sklep.pop("chleb")
# print(sklep)
#
# # modyfikacja wartosci
# sklep["cola"] = 5.50
# print(sklep)
#
# # dlugosc slownika
# print(len(sklep))