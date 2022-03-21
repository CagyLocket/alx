# Ex. 46-3
#
# ❑ Zaprojektuj grę w kółko i krzyżyk
# ❑ W programie obowiązują klasyczne zasady gry ❑ Układ planszy 3x3
# ❑ Wykorzystaj poznane Ci mechanizmy

# Zadanie 46_3 (OiX) proszę rozbudować o:
# 1. wszystkie warunki wygrane
# 2. jeżeli gracz postawi swój symbol na polu zajętym to traci kolejkę
# 3. jeżeli są wszystkie pola zajęte i nie ma wygranej to jest remis


def game():

    gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

    gracz = "X"
    count = 0

    while(True):

        def print_board():
            for i in gra:
                for j in i:
                    print(j, end=" ")
                print()
        print_board()

        wsp = input(f"Gracz {gracz} podaj wsplorzedne: ") # "12"

        wspX = int(wsp[0])
        wspY = int(wsp[1])

        if (gra[wspX][wspY] == "*"):
            gra[wspX][wspY] = gracz
            count += 1
        else:
            print(f"Miejsce zajęte. Gracz {gracz} traci kolejkę.")
            if (gracz == "X"):
                gracz = "O"
            else:
                gracz = "X"
            continue
        # print(count)

        # 8 conditions for winning the game by X or O
        if (count >= 3):
            if (gra[0][0] == gra[0][1] == gra[0][2] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[1][0] == gra[1][1] == gra[1][2] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[2][0] == gra[2][1] == gra[2][2] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[0][0] == gra[1][0] == gra[2][0] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[0][1] == gra[1][1] == gra[2][1] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[0][2] == gra[1][2] == gra[2][2] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[0][0] == gra[1][1] == gra[2][2] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break

            elif (gra[0][2] == gra[1][1] == gra[2][0] != "*" ):
                print_board()
                print("--- koniec gry ---")
                print(f"Gracz {gracz} wygrał. ")
                break
        if (count == 9):
            print_board()
            print("Remis")
            break

        #zamiana graczy
        if(gracz == "X"):
            gracz = "O"
        else:
            gracz = "X"


game()