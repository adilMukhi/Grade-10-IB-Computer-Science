"""
5) polygons.py Write a program that allows a user to choose from a menu whether to calculate the area of a
rectangle, triangle, circle etc. Ask the user for dimensions appropriate to the request. Next, calculate the
area using one of several functions. Display the menu as part of the main program, but the dimensions
and the calculations for each of the shapes should be in their own shape-specific functions.
"""
import math

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width
def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height
def circle_area():
    rOrd = input("Radius (1) or diameter (2): ")
    if rOrd == "1":
        radius = float(input("Enter the radius of the circle: "))
    if rOrd == "2":
        radius = float(input("Enter the diameter of the circle: ")) / 2
    return math.pi * radius ** 2
def square_area():
    side = float(input("Enter the side length of the square: "))
    return side ** 2

print("Welcome to the Area Calculator!")
print("Please choose a shape to calculate the area for:")
print("1. Rectangle")
print("2. Triangle")    
print("3. Circle")  
print("4. Square")  
shape = int(input("Enter your choice (1-4): "))
if shape == 1:
    print(round(rectangle_area(),2))
elif shape == 2:
    print(round(triangle_area(), 2))
elif shape == 3:
    print(round(circle_area(), 2))
elif shape == 4:
    print(round(square_area(), 2))
else:
    print("Invalid input. Please enter a valid choice.")