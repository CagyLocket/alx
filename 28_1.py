txt = input("Podaj dowolne zdanie:")

#policz ile jest znakow w zdaniu
ile_znakow = len(txt)

# policz ile jest spacji w zdaniu na 2 sposoby
# Sposób 1:
l_spacji_1 = txt.count(" ")

#Sposób 2:

rep = len(txt.replace(" ", ""))
print(rep)
l_spacji_2 = int(ile_znakow) - int(rep)

print(f"Liczba znaków: {ile_znakow}")

print(f"Liczba spacji: {l_spacji_1}")
print(f"Liczba spacji: {l_spacji_2}")



