#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str1 = "is"
greaterThanFive = "and is greater than 5"
lessThanSix = "and is less than 6 and not 0"
isZero = "and is 0"
lastDig = abs(number) % 10
if lastDig > 5:
    print(f"{str} {number} {str1} {lastDig} {greaterThanFive}")
elif lastDig < 6 and lastDig != 0:
    print(f"{str} {number} {str1} {lastDig} {lessThanSix}")
else:
    print(f"{str} {number} {str1} {lastDig} {isZero}")
