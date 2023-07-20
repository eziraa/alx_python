#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0
if (number >= 0):
    last = number % 10
else:
    last = ((-1 * number) % 10) * -1
msg = ""
if (last == 0):
    msg = "is 0"
elif (last > 5):
    msg = "is greater than 5"
else:
    msg = "is less than 6 and not 0"
print(f"Last digit of {number} is {last} and {msg}")
