import random
from decimal import *

k = input("How many random integers would you like to generate? ")
j = int(k)
total = 0

k = int(k)
while k > 0:
    randomNumber = random.randint(1, 1000)
    total += randomNumber
    k -= 1

average = round((total / j), 2)
print("The average is " + str(average))
