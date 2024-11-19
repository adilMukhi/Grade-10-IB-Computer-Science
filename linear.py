"""
3) linear.py Write a function that takes an x-value as a parameter and calculates a y-value for y =
3/7x + 5. Use this function in the main program to generate a table of values for x = –10..10.
"""

def linear(x):
    return round(3/7*x + 5,2)

for i in range (-10,11):
    print(f"x = {i}, y = {linear(i)}")