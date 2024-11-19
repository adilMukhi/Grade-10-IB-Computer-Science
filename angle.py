"""
angle.py Write a function called angle(a,b,c) that will determine the measure of the angle opposite
side a in a triangle given side lengths a, b, and c as parameters and prints the result.
Test your program with these values:
angle(3, 4, 5) => 37 degrees
angle(4, 3, 5) => 53 degrees
angle(5, 4, 3) => 90 degrees
"""
import math

def angle():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    cosA = (b**2 + c**2 - a**2) / (2*b*c)
    return int(round(math.degrees(math.acos(cosA)),0))

print(angle())