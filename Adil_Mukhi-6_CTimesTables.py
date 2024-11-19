"""
c) Times Tables.py – Write a program that takes in a posiƟve integer n, and prints an “n-Ɵmes table”
containing values up to n x n. For example, if the program reads the value 5, it should print
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
"""

n = int(input("Enter a positive integer: "))

for i in range (n):
    print(f"{n} x {i+1} = {n*(i+1)}")