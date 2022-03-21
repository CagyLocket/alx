# Ex. 67-3
#
# ❑ Zaprojektuj formularz rezerwacji biletu do kina.
# ❑ Wprowadzenie niepoprawnych danych powinno spowodować powtórne wprowadzenie
# nowych danych dla tego samego pola.
#
# ❑ Pytania:
#
# ❑ Podaj index kina (int)
# ❑ Podaj index filmu (int)
# ❑ Podaj ilość osób (int)
# ❑ Podaj swoje imię (str – tylko małe litery, bez polskich znaków)
#
# ❑ Podsumowanie rezerwacji


kina = ["Cinema-City", "Multikino"]
filmy = {0: ["Matrix", "Avatar", "Shrek"], 1: ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

while(True):

    while(True):
        print(f"Kina: {kina[0]} - 0, {kina[1]} - 1")
        try:
            kino = int(input("Podaj indeks kina: "))
        except ValueError:
            print("Niepoprawny indeks.")
            break

        except IndexError:
            print("Nipoprawny indeks.")
            break
        if (kino == 0):
            kino = kina[0]
            print(f"Wybrano kino: {kino}")
        elif (kino == 1):
            kino = kina[1]
            print(f"Wybrano kino: {kino}")
        else:
            print("Niepoprawny indeks.")
            continue
        break

    while(True):
        if (kino == kina[0]):
            kino = 0
            print(f"\nFilmy: {filmy[0][0]} - 0, {filmy[0][1]} - 1, {filmy[0][2]} - 2 ")
        elif (kino == kina[1]):
            kino = 1
            print(f"\nFilmy: {filmy[1][0]} - 0, {filmy[1][1]} - 1, {filmy[1][2]} - 2 ")

        try:
            film = int(input("Podaj indeks filmu: "))
        except ValueError:
            print("Niepoprawny indeks.")
            break

        if (film == 0):
            film = filmy[kino][0]
            print(f"Wybrano film: {film}")
        elif(film == 1):
            film = filmy[kino][1]
            print(f"Wybrano film: {film}")
        elif(film == 2):
            film = filmy[kino][2]
            print(f"Wybrano film: {film}")
        else:
            print("Niepoprawny indeks.")
            continue
        break

    while(True):
        try:
            ile = int(input("Podaj liczbę osób: "))
        except ValueError:
            print("Niepoprawna liczba osób.")
            continue

        if (ile == 0):
            print("Minimalna liczba osób to 1.")
            continue

        print(f"Liczba osób: {ile}")
        break

    while (True):

        imie = input("Podaj swoje imię: ")
        counter = 0

        for i in imie:
            if (i not in litery):
                print(f"Tylko małe litery, bez polskich znaków.")
                break
            else:
                counter += 1
                continue
        if (counter == len(imie)):
            print(f"Imię osoby rezerwującej: {imie}")
            break

    break

print("\nPODSUMOWANIE REZERWACJI:")
print(f"-----------------------")
print(f"kino: {kina[kino]}")
print(f"film: {film}")
print(f"liczba osób: {ile}")
print(f"Imię osoby rezerwującej: {imie}")
print(f"RAZEM DO ZAPŁATY: {cenaBilet * ile } zł.")
