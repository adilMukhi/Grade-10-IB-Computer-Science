"""
e) Factors.py – Write a program that asks the user for an integer between 1 to 50 and 
output all of its factors.
"""

num = int(input("Enter an integer between 1 and 50: "))

for i in range(1,51):
    if num % i == 0:
        print(i)