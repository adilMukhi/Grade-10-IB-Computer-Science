"""
6) BankRule.py - A bank has the following rule: if a customer has more than $1000 dollars in their checking account or
more than $1500 dollars in their savings account, then there is no service charge for wriƟng checks. Otherwise, there is a
$0.15 charge per check. Write a program that asks for the balance in each account and then writes out the service
charge.
"""

amount = float(input("Enter the balance in your checking account: $"))
savings = float(input("Enter the balance in your savings account: $"))

if amount >= 1000 or savings >= 1500:
    print("You have no service charge for writing checks.")
else:
    print("There is a $0.15 charge per check.")