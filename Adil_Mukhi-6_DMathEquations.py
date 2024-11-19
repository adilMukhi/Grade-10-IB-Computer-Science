"""
d) MathEquaƟons.py – Write a program that will output the value of the
math quesƟons to the right. Use one loop for each math quesƟon and
simply output a statement like “Answer for QuesƟon 1 is 5.18738“.
Round the answers to 5 decimal places.
"""
# Question 1
sum1 = 0

for i in range (1000):
    sum1 = sum1 + i + 1

ans1 = 1 / sum1
print (f"Answer for Question 1 is {round(ans1, 5)}")

# Question 2
import math

sum2 = 0

for i in range (100, 5001, 100):
    sum2 = sum2 + math.sqrt(i)

print(f"Answer for Question 2 is {round(sum2, 5)}")

# Question 3
sum3 = 1

for i in range (1,21):
    sum3 = sum3 * i

print(f"Answer for Question 3 is {round(sum3, 5)}")

# Question 4
sum4 = 0

for i in range (-12, 21):
    sum4 = sum4 + i**3

print(f"Answer for Question 4 is {round(sum4, 5)}")