"""
8) Cookies.py - Write a program that asks a user how many boxes of cookies they want to order. There are three types
of cookies: Chocolate Chip, Oatmeal, and Shortbread. If the user orders 5 boxes of one type or 10 boxes in total, they
will receive a 10% discount. Write a program that outputs the total cost including tax. Assume each box of cookies cost
$4.95.
"""
cost = 4.95

CCamount = int(input("How many boxes of Chocolate Chip cookies do you want to order? "))
OCamount = int(input("How many boxes of Oatmeal cookies do you want to order? "))
SBamount = int(input("How many boxes of Shortbread cookies do you want to order? "))

totalC = CCamount + OCamount + SBamount

if totalC >= 10 or (CCamount >= 5 or OCamount >= 5 or SBamount >= 5):
    cost = cost * 0.9 * totalC
else:
    cost = cost * totalC

print("The total cost is $", cost)