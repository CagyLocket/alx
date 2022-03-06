import pymysql


try:
    conn = pymysql.connect(host="localhost", user="root", password="Mojesilnehaslo123", database="db93", charset="utf8")
    c = conn.cursor()
    print("Połączenie OK")
except:
    print("Błąd połączenia")


def dodaj(imie, nazwisko, pensja):

    sql = f"INSERT INTO pracownicy(imie, nazwisko, pensja) VALUES ('{imie}', '{nazwisko}', {pensja})"
    c.execute(sql)

    dec = input("Czy dodać dane do bazy? T/N").upper()
    if(dec == "T"):
        conn.commit()
        print("Dane pomyślnie dodane")
    else:
        conn.rollback()
        print("Operacja anulowana")


def pokaz():
    sql = f"SELECT * FROM pracownicy"
    c.execute(sql)
    dane = c.fetchall()
    print(dane)
    count = 0
    for row in dane:
        count += 1
        print(count, row[1], row[2], row[3])

def usun(nazwisko):
    sql = f"SELECT * FROM pracownicy WHERE pracownicy.nazwisko='{nazwisko}'"
    c.execute(sql)
    dane = c.fetchall()
    # print(dane[0][0]) # zwraca ID użytkownika

    sql = f"DELETE FROM pracownicy WHERE idpracownicy='{dane[0][0]}' "
    c.execute(sql)

    dec = input("Czy usunąć {nazwisko} z bazy? T/N").upper()
    if (dec == "T"):
        conn.commit()
        print(f"Pomyślnie uzunięto użytkownika {nazwisko} z bazy")
    else:
        conn.rollback()
        print("Operacja anulowana")


def zmien(nazwisko):
    sql = f"SELECT * FROM pracownicy WHERE pracownicy.nazwisko='{nazwisko}'"
    c.execute(sql)
    dane = c.fetchall()
    # print(dane)

    if len(dane) == 0:
        print("Nie ma takiego użytkownika w bazie")
    else:
        nowe_imie = input("Podaj nowe imię:")
        nowe_nazwisko = input("Podaj nowe nazwisko:")
        nowa_pensja = int(input("Podaj nową pensję:"))

        sql = f"UPDATE pracownicy SET imie='{nowe_imie}', nazwisko='{nowe_nazwisko}', pensja={nowa_pensja} WHERE idpracownicy={dane[0][0]}"
        c.execute(sql)
        dec = input(f"Czy usunąć {nazwisko} z bazy? T/N").upper()
        if (dec == "T"):
            conn.commit()
            print(f"Pomyślnie zaktualizowano użytkownika {nowe_nazwisko} z bazy")
        else:
            conn.rollback()
            print("Operacja anulowana")


#*

def szukaj(fraza):
    sql = f"SELECT * FROM pracownicy WHERE nazwisko LIKE '%{fraza}%' OR imie LIKE '%{fraza}%' "
    c.execute(sql)
    dane = c.fetchall()
    # print(dane)
    count = 0
    for row in dane:
        count += 1
        print(count, row[1], row[2], row[3])


while (True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, S*-szukaj, K-koniec").upper()

    if (menu == "D"):
        imie = input("Podaj imię:")
        nazwisko = input("Podaj nazwisko:")
        pensja = int(input("Podaj pensję:"))

        dodaj(imie, nazwisko, pensja)


    elif (menu == "P"):
        pokaz()

    elif (menu == "U"):
        nazwisko = input("Podaj nazwisko:")
        usun(nazwisko)

    elif (menu == "Z"):
        nazwisko = input("Podaj nazwisko:")
        zmien(nazwisko)

    elif (menu == "S"):
        fraza = input("Podaj szukaną frazę:")
        szukaj(fraza)

    elif (menu == "K"):
        break