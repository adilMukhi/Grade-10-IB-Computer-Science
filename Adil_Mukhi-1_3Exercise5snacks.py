# Adil Mukhi - Sep 24, 2024
# 1.3 Input 5. Exercise1.3snacks
"""
Cineplex Odeon charges $4.29 for a bag of popcorn, $3.49 for a bag/box of candy, and $1.99 for pop.

(a) Create a program that prompts the employee for the amount of popcorn, candy, and pop a customer
will buy and display the total, the tax (13% HST), and the grand total. The output should look something
like this.

(b) Modify the program to prompt the employee for the amount tendered and then display the change
due. Your final product should look something like this:
"""

# CODE FOR PART A
"""
amountOfPopcorn = int(input("Enter the amount of popcorn: "))
amountOfCandy = int(input("Enter the amount of candy: "))
amountOfPop = int(input("Enter the amount of pop: "))

subtotal = round(((4.29 * amountOfPopcorn) + (3.49 * amountOfCandy) + (1.99 * amountOfPop)),2)
hst = round((subtotal * 0.13),2)
grandTotal = round((subtotal + hst), 2)

print("Subtotal ", "$", subtotal)
print("HST ", "$", hst)
print("Grand Total ", "$", grandTotal)
"""

amountOfPopcorn = int(input("Enter the amount of popcorn: "))
amountOfCandy = int(input("Enter the amount of candy: "))
amountOfPop = int(input("Enter the amount of pop: "))

subtotal = round(((4.29 * amountOfPopcorn) + (3.49 * amountOfCandy) + (1.99 * amountOfPop)),2)
hst = round((subtotal * 0.13),2)
grandTotal = round((subtotal + hst), 2)

print("Subtotal ", "		$", subtotal)
print("HST ", "			$", hst)
print("Grand Total ", "		$", grandTotal)

amountTendered = float(input("Amount Tendered		$ "))
changeDue = round((amountTendered - grandTotal),2)

print("Change Due:		$", changeDue)