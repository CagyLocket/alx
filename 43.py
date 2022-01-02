# Cwiczenie 43 #

# Napisz program, który oblicza wartość współczynnika BMI wg wzoru (waga /
# wzrost**2). Wzrost podawany jest w metrach.
#
# Jeżeli wynik jest w przedziale (18.5 – 24.9) to wypisuje „waga prawidłowa”, jeżeli
# poniżej to „niedowaga”, jeżeli powyżej to „nadwaga”.



# Get a user's mass in kg
raw_input_mass = input("Podaj swoją wagę w kilogramach:")

# Check if the input is a digit
if(raw_input_mass.replace(".", "", 1).isdigit() == False):
    print("Pamiętaj, że trzeba wpisać swoją wagę jako liczbę i użyć kropki zamiast przecinka. \n"
          "Jeżeli ważysz np. 40.5 kg to wpisz 40.5 \n")
    raw_input_mass = input("Podaj swoją wagę w kilogramach:")
else:
    mass = float(raw_input_mass)
    # print(mass)

mass = float(raw_input_mass)

# Get a user's height in meter
raw_input_height = input("Podaj swój zwrost w metrach:")

# Check if the input is a digit
if(raw_input_height.replace(".", "", 1).isdigit() == False):
    print("Pamiętaj, że trzeba wpisać swój wzrost jako liczbę i użyć kropki zamiast przecinka. \n"
          "Jeżeli Twój zwrost to np. 1.85 m to wpisz 1.85 \n")
    raw_input_height = input("Podaj swój zwrost w metrach:")
else:
    height = float(raw_input_height)
    # print(height)

height = float(raw_input_height)

# Calculate user's BMI
BMI = round(mass / (height ** 2), 1)
#print(BMI)

# Print in a terminal BMI evaluation for the user's input
if(BMI >= 18.5 and BMI <= 24.9):
    print(f"Twój wskaźnik BMI to {BMI} - waga prawidłowa")
elif(BMI < 18.5):
    print(f"Twój wskaźnik BMI to {BMI} - niedowaga")
else:
    print(f"Twój wskaźnik BMI to {BMI} - nadwaga")
