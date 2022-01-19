kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

while(True):

    while(True):
        kino = int(input("Podaj indeks kina: "))
        print(f"Wybrano kino {kina[kino]}")
        except:
            print("Błąd")
        else:
             break

    while(True):
        film = int(input("Podaj indeks filmu: "))
        if (film == 0):
            film_rezerwacja = filmy[0]
        elif(film == 1):
            film_rezerwacja = film[1]
        else:
            print("niepoprawny indeks!")
        break
        # print(film_rezerwacja)

    while(True):
        ile = int(input("Podaj ilość osób: "))
        break
        # print(ile)


    while(True):
        imie = input("Podaj swoje imię: ")
        break
        print(imie)

    break

print("PODSUMOWANIE REZERWACJI:")
print(f"kino: {kino_rezerwacja}")
print(f"film: {film_rezerwacja}")
print(f"liczba_osób: {ile}")
print(f"Imię osoby rezerwującej: {imie}")

