# Adil Mukhi - Sep 25, 2024
# 1.4 Math Calculations 4. Exercise1.4areaPerimeter-Write

"""
4. Exercise1.4areaPerimeter-Write a program that will ask the user for the length and width of a
rectangle. The program will then calculate the perimeter and area and output the results clearly. Use
variables for the words marked in bold.
"""

length = int(input("What is the length? "))
width = int(input("What is the width? "))

area = round((length * width),3)
perimeter = round(((length*2) + (width*2)),3)

print ("The area is", area,"cm^2.")
print ("The perimeter is", perimeter,"cm.")