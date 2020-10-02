#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
number = int(input("Enter a number: "))
cube = number ** (1/3)
square = number ** 0.5
sq2 = round(square,8)%2
c2 = round(cube,8)%2


if int(b + 0.5) ** 2 == a and a ** 1/3 == c:
  print(str(a) + " is both a perfect square and a perfect cube.")
elif int(b + 0.5) ** 2 == a:
  print(str(a) + " is only a perfect square.")
elif a ** 1/3 == c:
  print(str(a) + " is only a perfect cube.")

