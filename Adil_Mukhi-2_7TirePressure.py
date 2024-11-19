"""
7) TirePressure.py - The front Ɵres of a car should both have the same pressure. Also, the rear Ɵres of a car should both
have the same pressure (but not necessarily the same pressure as the front Ɵres.) Write a program that reads in the
pressure of the four Ɵres and writes a message that says if the inflaƟon is OK or not.
Enter right front pressure: 38
Enter left front pressure: 38
Enter right rear pressure: 42
Enter left rear pressure: 42
Inflation is OK
"""

front1 = int(input("Enter right front pressure: "))
front2 = int(input("Enter left front pressure: "))
back1 = int(input("Enter right rear pressure: "))
back2 = int(input("Enter left rear pressure: "))

if front1 == front2 and back1 == back2:
    print("Inflation is OK")
else:
    print("Inflation is not OK")