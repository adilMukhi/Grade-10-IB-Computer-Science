"""
7) ground.py Determine the time for an object, thrown with velocity v from an initial height h, to hit the
ground using the formula:−4.9t^2 + vt + h = 0. Hint: Use quadratic formula. Name the function
find_time(v, h) and return time. In the main program, test your function with these values: v=10,
h=1 => answer should be 2.14.
"""
import math

def find_time(v, h):
    # Coefficients for the quadratic equation at^2 + bt + c = 0
    a = -4.9
    b = v
    c = h
    
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return None  # No real solutions if discriminant is negative
    
    # Calculate both solutions of the quadratic equation
    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    # Return the positive time value, as time cannot be negative
    time = max(t1, t2)
    
    return round(time, 2)

# Test the function with v=10, h=1
v = float(input("Enter the initial velocity (v): "))
h =  float(input("Enter the initial height (h): "))
print(find_time(v, h))