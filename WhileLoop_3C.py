"""
c) Write a program that will count how many weekdays and how many weekends are inpuƩed by the user.
E.g. as the user to input days of the week, (e.g. “Monday, Tuesday, Saturday, etc.”). They should enter
“end” to stop the program. Output the total number of weekday days and weekend days there are.
Hint: have a weekdayCounter and a weekEndCounter
"""
weekdayCounter = 0
weekEndCounter = 0
day = ""

while day != "end":
    day = input("Enter a day (or 'end' to stop): ")
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        weekdayCounter += 1
    if day == "Saturday" or day == "Sunday":
        weekEndCounter += 1

print(f"Number of weekday days: {weekdayCounter}")
print(f"Number of weekend days: {weekEndCounter}")