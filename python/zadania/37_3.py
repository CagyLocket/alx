# Cwiczenie 37_3 #

# Napisz program, który liczy pole albo obwód prostokąta.
# Ile wynosi pierwszy bok prostokąta ? 43
# Ile wynosi drugi bok prostokąta ? 12
# Co chcesz policzyć ? 1 – pole, 2 – obwód 1
# Pole prostokąta to: 516


# Get length values from a user
a = float(input("Ile wynosi pierwszy bok prostokąta?"))
b = float(input("Ile wynosi drugi bok prostokąta?"))

# User to choose what to calculate
q = int(input("Co chcesz policzyć? 1 - pole, 2 - obwód"))

# Calculate object's area or permieter
if q == 1:
    area = round(a * b, 1)
    print(f"Pole prostokąta to: {area}")

elif(q == 2):
    perimeter = round(a + a + b + b, 1)
    print(f"Obwód prostokąta to: {perimeter}")
else:
    print("Podałeś/aś nieprawidłową liczbę.")

