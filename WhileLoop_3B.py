"""
b) Write a program that will add up all numbers between 1 and 100 and output only the sum, 
at the end.
"""

num = 1
sum = 0
while num <= 100:
    sum = sum + num
    num += 1
print(sum)