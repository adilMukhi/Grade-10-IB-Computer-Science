"""
Fibonacci.py  Write a program that outputs the first N numbers of the Fibonacci sequence, starƟng with 1,
1. For example, if the user enters 7, your output should be “1 1 2 3 5 8 13”
"""
"""
n = int(input("Enter the number of Fibonacci numbers to generate: "))
num1, num2 = 1, 1

for i in range(n):
    if (i == 0) and (n >= 2):
        print("1, 1", end=" ")
    elif (i == 0) and (n == 1):
        print("1", end=" ")
    num3 = num2 + num1
    num1 = num2
    num2 = num3
    if i != 0:
        print(num3, end="")
"""
n = int(input("Enter the number of Fibonacci numbers to generate: "))

num1 = 1
num2 = 1

for i in range(n):
    if i == 0 and n >= 1:
        print("1", end=" ")
    elif i == 1 and n >= 2:
        print("\b, 1", end=" ")
    else:
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        print(f", {num2}", end="")