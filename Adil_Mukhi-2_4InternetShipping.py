"""
4) InternetShipping.py - Write a program to take orders from the Internet. Your program should ask for the item, its
price, and if overnight shipping is wanted. Regular shipping for totals under $10 is $2.00; for totals $10 or more, shipping
is $3.00. For overnight delivery add $5.00.
Enter the item: Socks for Dolby
Enter the price: $4.50
Overnight delivery (0==no, 1==yes: 1
Invoice:
Socks for Dolby $4.50
Shipping $7.00
Total $11.50
"""

item = input("Enter the item: ")
price = float(input("Enter the price: $"))
overnight = int(input("Overnight delivery (0==no, 1==yes): "))

if price < 10:
    if overnight == 1:
        shipping = 7.00
    else:
        shipping = 2.00
else:
    if overnight == 1:
        shipping = 8.00
    else:
        shipping = 3.00

print("Invoice:")
print(item, " $", price)
print("Shipping $", shipping)
print("Total $", price + shipping)