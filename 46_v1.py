# Cwiczenie 46_v1 #

# Create an empty set for random digits
numb_set = set()

# Declare 6 random variables and add them into the set()
import random
numb_1 = random.randint(-100,100)
numb_set.add(numb_1)
numb_2 = random.randint(-100,100)
numb_set.add(numb_2)
numb_3 = random.randint(-100,100)
numb_set.add(numb_3)
numb_4 = random.randint(-100,100)
numb_set.add(numb_4)
numb_5 = random.randint(-100,100)
numb_set.add(numb_5)
numb_6 = random.randint(-100,100)
numb_set.add(numb_6)

# Create supporting variables
current_min = 0
current_max = 0

# Find max
if(numb_1 > current_max):
    current_max = numb_1

if(numb_2 > current_max):
    current_max = numb_2

if(numb_3 > current_max):
    current_max = numb_3

if(numb_4 > current_max):
    current_max = numb_4

if(numb_5 > current_max):
    current_max = numb_5

if(numb_6 > current_max):
    current_max = numb_6

# Find min
if (numb_1 < current_min):
    current_min = numb_1

if (numb_2 < current_min):
    current_min = numb_2

if (numb_3 < current_min):
    current_min = numb_3

if (numb_4 < current_min):
    current_min = numb_4

if (numb_5 < current_min):
    current_min = numb_5

if (numb_6 < current_min):
    current_min = numb_6

# Outcome
print(f"a = {numb_1}; b = {numb_2}; c = {numb_3}; d = {numb_4}, e = {numb_5}, f = {numb_6}; ")
print(f"Min to: {current_min}")
print(f"Max to: {current_max}")


