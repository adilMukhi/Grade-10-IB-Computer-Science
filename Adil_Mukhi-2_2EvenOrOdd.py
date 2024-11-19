"""2) EvenOrOdd.py - Ask the user to enter a posiƟve integer greater than 0. Tell them if their number is even or odd.
Remember that you can use the modulo operator to do this!"""

number = int(input("Enter a positive integer greater than 0: "))
if number > 0:
    if number % 2 == 0:
        print("The number", number, "is even.")
    else:
        print("The number", number, "is odd.")
else:
    print("Invalid input. Please enter a positive integer greater than 0.")