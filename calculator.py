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
        floats = []
        for token in tokens[1:]:
            if len(tokens) > 1:
                token = float(token)
                floats.append(token)

        if tokens[0] == "q":
            break

        elif tokens[0] == "+":
            print add(floats)
        
        elif tokens[0] == "-":
            print subtract(floats)
        
        elif tokens[0] == "*":
            print multiply(floats)

        elif tokens[0] == "/":
            print divide(floats)

        elif tokens[0] == "square":
            if len(floats) > 1:
                print "Error! Square only takes one argument!"
            else:
                print square(floats[0])

        elif tokens[0] == "cube":
            if len(floats) > 1:
                print "Error! Cube only takes one argument!"
            else:
                print cube(floats[0])

        elif tokens[0] == "pow":
            print power(num1, num2)

        elif tokens[0] == "mod":
            print mod(num1, num2)


print " Enter a math problem like this: + 2 2" 
prefix_calculations()

