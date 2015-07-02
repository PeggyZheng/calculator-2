"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def prefix_calculations():
    while True:
        user_input = raw_input(">")
        tokens = user_input.split(" ")
        if len(tokens) > 1:
            num1 = float(tokens[1])
        if len(tokens) > 2:
            num2 = float(tokens[2])

        if tokens[0] == "q":
            break

        elif tokens[0] == "+":
            print add(num1, num2)
        
        elif tokens[0] == "-":
            print subtract(num1, num2)
        
        elif tokens[0] == "*":
            print multiply(num1, num2)

        elif tokens[0] == "/":
            print divide(num1, num2)

        elif tokens[0] == "square":
            print square(num1)

        elif tokens[0] == "cube":
            print cube(num1)

        elif tokens[0] == "pow":
            print power(num1, num2)

        elif tokens[0] == "mod":
            print mod(num1, num2)


print " Enter a math problem like this: + 2 2" 
prefix_calculations()

