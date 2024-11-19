"""3) DeathValley.py - You have decided to visit the ghost towns in California's Death Valley - the hoƩest place in North
America! Last Chance Gas staƟon sits on Route 190 on the edge of Death Valley. There is no other gas staƟon for 350 km.
You are to write a program to help drivers decide if they need gas.
The program should ask for: The capacity of the gas tank, in liters. E.g. 50 L is a typical gas tank
The indicaƟon of the gas gauge in percent (full= 100%, three quarters full = 75%) E.g. The user would enter 30 for 30%
The fuel consumpƟon for the vehicle in litres per 100km of the car. E.g. 9.7L per 100km is a typical fuel consumpƟon
The program then writes out "Get Gas" or "Safe to Proceed" depending on if the car can travel the necessary 350 km
with the gas remaining in the tank."""

capacity = float(input("Enter the capacity of your gas tank in liters: "))
percent = float(input("Enter the percentage of your gas gauge (e.g., 30 for 30%): ")) / 100
consumption = float(input("Enter your fuel consumption in litres per 100 km: "))

distance = capacity * percent * 350 / consumption

if distance >= 350:
    print("Safe to Proceed")
else:
    print("Get Gas")