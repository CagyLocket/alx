# Cwiczenie 36_4 #

# Zaprojektuj program który będzie losował dwie liczby i znak działania
# ❑ Liczby losowane są w zakresie (1-9)
# ❑ Znak działania dotyczy operacji (+, -, *)
#
# Po wylosowaniu ww. danych komputer zadaje pytanie np.:
# Ile to jest 2 + 6 = ? lub
# Ile to jest 8 * 3 = ?
# ❑ Użytkownik udziela odpowiedź która jest sprawdzana przez komputer.
# ❑ Ostatecznie użytkownik otrzymuje informację czy udzielił poprawną odpowiedź czy błędna.


# Import libs
import random
import operator
# Operators as functions
# from https://docs.python.org/3/library/operator.html

# Declare operators
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

# Get random variables
random_operator = random.choice(list(operators.keys()))
numb_1 = random.randint(1,9)
numb_2 = random.randint(1,9)

# Multiplication of random variables
result_computer = operators[random_operator](numb_1, numb_2)

# User to give a result of multiplication
result_user = int(input(f"Ile to jest {numb_1} {random_operator} {numb_2} = ?"))

# Check user's result and give feedback
if(result_user == result_computer):
    print("Poprawna odpowiedź!")
else:
    print(f"Niestety to błędna odpowiedź. Poprawny wynik to: {numb_1} {random_operator} {numb_2} = {result_computer}")

