#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
number= int(input("Enter a number: "))

if number < 0 or number ==0:
  print(str(number) + " is not a positive integer.")
elif number > 0:
  print(str(number) + " is not a positive integer.")
