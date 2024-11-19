"""
4) sum.py Write a function that takes
 a positive integer n as a parameter and returns the sum 1 + 2 + ... + n.
"""

def summation():
    try:
        x = int(input("Enter a positive integer: "))
        if x <= 0 or x > 10000000000:
            print("Please enter a positive integer.")
            return summation()
    except:
        print("Invalid input. Please enter a positive integer.")
        return summation()
    sum = 0
    for i in range(1, x+1):
        sum = sum + i
    return sum

print(summation())