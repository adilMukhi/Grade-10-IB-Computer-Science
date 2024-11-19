# Adil Mukhi - Sep 25, 2024
# 1.5 More Math Calculations 2. Exercise1.5fourDigits

"""
2. Exercise1.5fourDigits - Write a program that prompts the user for a 4-digit positive integer value
(e.g., from 1000 to 9999). Use integer division by 1000 to isolate the first digit. Use the remainder to
isolate the remaining three digits. Repeat this process using division by 100, 10, and 1 to isolate the
remaining digits. The goal of the program is to output the list of digits.
For example: Please enter a positive, 4-digit number (1000 to 9999): 2358

The digits of 2358 are 2, 3, 5, and 8
"""

number = int(input("Give 4-digit positive integer value (e.g., from 1000 to 9999): "))

digitOne = (number//1000)
digitTwo = ((number%1000)//100)
digitThree = (((number%1000)%100)//10)
digitFour = ((((number%1000)%100)%10)//1)

print ("The digits of ", number," are ",digitOne,", ",digitTwo,", ",digitThree,", and ",digitFour,".")