#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = abs(number) % 10

if lastDig > 5:
    print(f"Last digit of {number} is {lastDig} and is greater than 5\n")
elif lastDig < 6 and lastDig != 0:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0\n")
else:
    print(f"Last digit of {number} is {lastDig} and is 0\n")