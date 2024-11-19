# Adil Mukhi - Sep 24, 2024
# 1.4 Math Calculations 3. Exercise1.4areaCircumference

"""
3. Exercise1.4areaCircumference-Write a program that will ask the user for the radius of a circle. The
program will then calculate the circumference and area of the circle and output the results clearly. Use
a variable for words marked in bold. Use a constant for pi.
"""

import math

radiusOfCircle = float(input("Enter Radius: "))
curicumference = 2 * math.pi * radiusOfCircle
area = math.pi * radiusOfCircle**2

print("The curcumference is: ", round(curicumference, 3))
print("The area is: ", round(area, 2))