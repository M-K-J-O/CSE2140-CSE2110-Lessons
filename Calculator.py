# Calculator.py
"""
Title: Calculator(that's 100000000000000000x worse than just using a actual calculator)
Author: MARCO OU
DATE: 2/6/2023
"""

print("")
print("===------Calculator-----===")
print("")
USER_START = input("Start? y/n: ")
USER_OUTPUT = 0

if USER_START == "y":
    print("Addition:+, Subtraction: -, Multiplication: *, Division: /, Modulus: %, Floor Division: //, Power: **")

while USER_START == "y":
    USER_FIRST_NUMBER = input("Enter a number: ")
    USER_FIRST_NUMBER = float(USER_FIRST_NUMBER)
    USER_SECOND_NUMBER = input("Enter second number: ")
    USER_SECOND_NUMBER = float(USER_SECOND_NUMBER)
    USER_SYMBOL = input("Enter a Symbol :")

    if USER_SYMBOL == "+":
        USER_OUTPUT = float(USER_FIRST_NUMBER) + float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "-":
        USER_OUTPUT = float(USER_FIRST_NUMBER) - float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "*":
        USER_OUTPUT = float(USER_FIRST_NUMBER) * float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "/":
        USER_OUTPUT = float(USER_FIRST_NUMBER) / float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "%":
        USER_OUTPUT = float(USER_FIRST_NUMBER) % float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "//":
        USER_OUTPUT = float(USER_FIRST_NUMBER) // float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
    if USER_SYMBOL == "**":
        USER_OUTPUT = float(USER_FIRST_NUMBER) ** float(USER_SECOND_NUMBER)
        print(USER_OUTPUT)
