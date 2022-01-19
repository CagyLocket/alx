
while(True):

    while(True):
        try:
            liczba1 = float(input("Podaj liczba 1:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    while (True):
        try:
            liczba2 = float(input("Podaj liczba 2:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("Nie dzielimy przez zero !")
    except:
        print("Nieoczekiwany blad")
    else:
        print("....")
    finally:
        print("TU BLOK FINALLY")



# Pierwszy kod
while(True):

    while(True):
        try:
            liczba1 = float(input("Podaj liczba 1:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    while (True):
        try:
            liczba2 = float(input("Podaj liczba 2:"))
        except ValueError:
            print("Wprowadzamy tylko liczby !!")
        else:
            break

    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("Nie dzielimy przez zero !")
    except:
        print("Nieoczekiwany blad")
    else:
        print("....")
    finally:
        print("TU BLOK FINALLY")








