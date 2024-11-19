# Adil Mukhi - Sep 25, 2024
# 1.4 Math Calculations 5. Exercise1.4timeConvert

"""
5. Exercise1.4timeConvert- Write a program that reads a time interval in hours, minutes, and seconds,
and converts this measurement to hours only. Assume that the user is entering a reasonable number for
minutes (between 0 and 59) and a reasonable number for seconds (between 0 and 59).
For example, if the inputs values were 13 hours and 15 minutes and 30 seconds, the output should be
something like: 13 hours, 15 minutes, 30 seconds is 13.26 hours
"""

hours = int(input("How many hours? "))
minutes = int(input("How many minutes? "))
sec = int(input("How many seconds? "))

totalHours = round(float(hours + (minutes/60) + (sec/3600)),2)

print (hours, "hours,", minutes, "minutes,", sec, "seconds is", totalHours, "hours") 