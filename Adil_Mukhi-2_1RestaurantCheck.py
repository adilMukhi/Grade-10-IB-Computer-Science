"""
1) RestaurantCheck.py - Prepare a check for someone eaƟng lunch in a restaurant. Have the user enter the cost of their
meal. If the meal costs more than $4.00 then add an 8% sales tax to the total.
"""
meal_cost = float(input("Enter the cost of your meal: "))
if meal_cost > 4.00:
    tax = meal_cost * 0.08
    total_cost = meal_cost + tax
    print("Your total cost including tax is:", round(total_cost, 2))
else:
    print("Your total cost is:", round(meal_cost,2))
