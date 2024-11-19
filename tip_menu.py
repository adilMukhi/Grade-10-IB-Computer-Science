"""
2) tip_menu.py Write a function to present the user with 4 tip options (10%, 15%, 20% and user input). The
function should return the calculated amount of tips rounded to two decimals. Your main program will
then use this value to calculate the total restaurant bill.
"""
total = round(float(input(f"Enter the total bill amount: ")),2)

def options():
    try:
        print("Tip options:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        print("4. Custom tip")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            return total * 0.10
        elif choice == 2:
            return total * 0.15
        elif choice == 3:
            return total * 0.20
        custom_tip = float(input("Enter the custom tip percentage: "))
        return total * (custom_tip / 100)
    except:
        print("Invalid input. Please enter a valid choice.")
        return options()

tips = round(options(),2)
print(f"Your cost is ${total}, plus ${tips} in tips, for a total of ${total + tips}.")