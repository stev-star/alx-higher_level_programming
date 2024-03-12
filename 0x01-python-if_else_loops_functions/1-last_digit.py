#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# convert the  number into a string
num_string = str(number)

# get the last digit from the number string
last_digit = num_string[-1]

# where the number is negative
if number < 0:
    last_digit = "-" + last_digit

# print the original output
print(f"Last digit of {number} is {last_digit} and", end=" ")

# check whether it satisfied the specified condition
if int(last_digit) > 5:
    print(f"is greater than 5")
elif int(last_digit)  == 0:
    print(f"is 0")
else:
    print(f"is less than 6 and not 0")
