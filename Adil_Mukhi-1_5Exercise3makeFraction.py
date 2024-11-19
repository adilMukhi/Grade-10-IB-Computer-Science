# Adil Mukhi - Sep 25, 2024
# 1.5 More Math Calculations 3. Exercise1.5makeFraction


"""
3. Exercise1.5makeFraction - To change an improper fraction into a mixed fraction, you can use
integer division and the remainder operator (modulo). Write a program that will allow the user to enter
two integer values, a numerator and denominator. The program should output these values as an improper
fraction, and then output the equivalent mixed fraction.
For example: Enter the numerator: 8
Enter the denominator: 3
8 / 3 is equivalent to 2 and 2 / 3
"""

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

num1 = numerator // denominator
num2 = numerator % denominator

print (numerator, "/", denominator, "is equivalent to", num1, "and", num2, "/", denominator)