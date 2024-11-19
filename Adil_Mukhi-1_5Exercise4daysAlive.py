# Adil Mukhi - Sep 25, 2024
# 1.5 More Math Calculations 4. Exercise1.5_daysAlive

"""
4. Exercise1.5_daysAlive – Create a program that calculates the number of days you have been alive and
the number of hours of your life that you have spent sleeping. Assume that you sleep 8 hours each night.
To simplify the problem, assume that there are 30 days in each month and 365 days in each year. The
output should look something like this:
Enter your birthday:
Year: 1974
Month: 05
Day: 08
Enter today’s date:
Year: 2011
Month: 09
Day: 26
"""

print("Enter your birthday:")
year1 = int(input("Year: "))
month1 = int(input("Month: "))
day1 = int(input("Day: "))
print(" ")
print("Enter today’s date:")
year2 = int(input("Year: "))
month2 = int(input("Month: "))
day2 = int(input("Day: "))

totalDays = ((year2-year1)*365) + ((month2-month1)*30) + (day2-day1)

print("You have been alive for ",totalDays," days! You have slept for ",(totalDays*8)," hours!")