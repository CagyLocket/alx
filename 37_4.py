# Cwiczenie 37_4 #

# Napisz program, który liczy pole jakiejś figury ?
# Jaka figura ? 1 – prostokąt, 2 – trójkąt 2
# Podaj długość podstawy:
# Podaj wysokość trójkąta:
# Pole to:
# Podaj długość boku a: 5
# Podaj długość boku b: 10
# Pole prostokąta to: 50



# User to choose an object type
q = int(input("Jaka figura? 1 - prostokąt, 2 - trójkąt: "))

if(q == 1):
    # Get object's sides from a user
    a = float(input('Podaj długość boku a: '))
    b = float(input('Podaj długość boku b: '))

    # calculate an area.
    area_square = round(a * b, 1)
    print(f"Pole prostokąta to: {area_square}")

elif(q == 2):
    # Get a bottom side & height of a triangle from a user
    a = float(input('Podaj długość podstawy: '))
    h = float(input('Podaj wysokość trójkąta: '))

    # calculate the area.
    area_triangle = round(0.5 * a * h, 1)
    print(f"Pole trójkąta to: {area_triangle}")

else:
    print("Podałeś/aś nieprawidłową liczbę.")

