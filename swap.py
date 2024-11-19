"""
8) swap.py Write a function that takes in two numbers as parameter and inter-swaps them. For example, if a
= 6 and b = 3 then a, b = swap (6,3) would give the value 3 to a and 6 to b.
"""
def swap(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(swap(a, b))