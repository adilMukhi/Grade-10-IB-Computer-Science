# Adil Mukhi - Sep 25, 2024
# 1.5 More Math Calculations 5. Exercise1.5_makeChange

"""
5. Exercise1.5_makeChange -Create a program that displays the minimum number of coins necessary to
make change out of any dollar amount. The change can be made up of toonies, loonies, quarters, dimes,
nickels, and pennies. You will need to use both the division (/) and modulus operators(%) in order to
calculate the correct change. The output should look something like this:
Amount of Change: $1.86
Toonies: 0
Loonies: 1
Quarters: 3
Dimes: 1
Nickels: 0
Pennies: 1
"""

change = round(float(input("Amount of Change: ")),2)

numToonies = change//2
numLoonies = (change%2)//1
numQuarters = ((change%2)%1)//0.25
numDimes = (((change%2)%1)%0.25)//0.10
numNickels = ((((change%2)%1)%0.25)%0.10)//0.05
numPennies = (((((change%2)%1)%0.25)%0.10)%0.05)//0.01 

print("Toonies: ", int(numToonies))
print("Loonies: ", int(numLoonies))
print("Quarters: ", int(numQuarters))
print("Dimes: ", int(numDimes))
print("Nickels: ", int(numNickels))
print("Pennies: ", int(numPennies))