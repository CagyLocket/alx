# gra w za dużo za mało
import random

# int_los = random.randint(1,6)
# int_user = int(input("Podaj liczbę: "))

# print(int_los)
# print(int_user)

def game():
    int_los = random.randint(1, 6)
    int_user = int(input("Podaj liczbę: "))

    while(True):
        for x in range(5):
            if x < 5:
                if (int_los < int_user):
                    print("Podałeś za dużą liczbę")
                    int_user = int(input("Podaj liczbę: "))
                elif(int_los > int_user):
                    print("Podałeś za małą liczbę")
                    int_user = int(input("Podaj liczbę: "))
                else:
                    print("Gratulacje")
                    # break

                    q = input("Grasz dalej? Wpisz tak lub nie:")
                    print(q)
                    if (q == 'tak'):
                        game()
                    else:
                        print("Dziękuję za grę!")
                        break
        else:
            print("Przegrałeś")
            q = input("Grasz dalej? Wpisz tak lub nie:")
            print(q)
            if (q == 'tak'):
                game()
            else:
                print("Dziękuję za grę!")
                break
        break


game()