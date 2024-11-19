""""
5) QuadraƟcEquaƟon.py - Write a program that determines how many x-intercepts the quadraƟc equaƟon has aŌer
asking the user to input the values for a, b, and c. The program should show appropriate messages if:
a) the value of a is zero, and the equaƟon is not quadraƟc
b) there are 0 (when b2 − 4ac is negaƟve), 1 (b2 − 4ac is zero), or 2 (when b2 − 4ac is posiƟve) x-intercepts.
"""
import math

# a^2 + bx + c = 0
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

if a == 0:
    print("The value of a is zero, and the equation is not quadratic.")
elif ((b**2 - 4*a*c) < 0):
    print("There are zero x-intercepts.")
elif ((b**2 - 4*a*c) == 0):
    print("There is one x-intercept.")
elif ((b**2 - 4*a*c) > 0):
    print("There are two x-intercepts.")

