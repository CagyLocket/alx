# Cwiczenie 36_4v1 #

# Import libs
import random

# Get random variables
random_operator = random.randint(0,2)
numb_1 = random.randint(1,9)
numb_2 = random.randint(1,9)

# Calculations with random variables
if(random_operator == 0):
    result_computer = numb_1 + numb_2
    r_op = "+"
elif(random_operator == 1):
    result_computer = numb_1 - numb_2
    r_op = "-"
else:
    result_computer = numb_1 * numb_2
    r_op = "*"

# User to give a result of multiplication
result_user = int(input(f"Ile to jest {numb_1} {r_op} {numb_2} = ?"))

# Check user's result and give feedback
if(result_user == result_computer):
    print("Poprawna odpowiedź!")
else:
    print(f"Niestety to błędna odpowiedź. Poprawny wynik to: {numb_1} {r_op} {numb_2} = {result_computer}")

