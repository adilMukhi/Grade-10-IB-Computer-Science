"""
6) Code the following quesƟons on an IDE.
a) Grocery Bill.py - Write a program that asks a user how many items 
are on their grocery bill. Then ask the
user to enter the cost of each item. When the user is done, 
output the total cost of their groceries plus HST.
"""

num = int(input("How many items are on your grocery bill? "))
total = 0

for i in range(num):
    cost = float(input(f"Enter the cost of item {i+1}: "))
    total += cost

total_with_tax = total * 1.13
print(f"Total cost including tax: ${round(total_with_tax, 2)}")