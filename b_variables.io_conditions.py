#b_variables_io_conditionals.py
"""
Title: CS 10 Concept Review and Translation
Author: MARCO OU
Date: 2/2/2023
"""

# --- Header Name --- #

STRING = '7'
INTEGER = 7
FLOAT = 7.0

"""
print(type(STRING))
print(type(INTEGER))
print(type(FLOAT))
"""

# --- Type Casting --- #

NUMBER = "13" #String
INT_NUMBER = int(NUMBER) #Integer
FLOAT_NUMBER = float(NUMBER) #Float

print(type(NUMBER), type(INT_NUMBER), type(FLOAT_NUMBER))

# --- Inputs --- #

USER_IN = input("Enter a number: ")
USER_IN = int(USER_IN)
print(USER_IN)

if USER_IN > 10:
    print("Woah that's very big")
else:
    print("Woah that's so small")
print("Generic Statement")