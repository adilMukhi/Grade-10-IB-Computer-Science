"""
Marks.py - Write a program that reads five marks and computes the average. Modify the program to ask
the user how many marks there are. Modify the program to check if the mark entered is between 0 and
100. If the mark is not between 0 and 100, print an error message that says “You entered a mark that is not
between 0 and 100. The calculated average may not make sense.” Finally, modify the program to also
output the lowest and highest mark.
"""
mark = 0
Lmark = 0
Hmark = 0
avgMark = 0

for i in range (5):
    mark = int(input(f"Enter mark {i+1}: "))
    if mark < 0 or mark > 100:
        print("You entered a mark that is not between 0 and 100. The calculated average may not make sense.")
        break
    if mark < Lmark or i == 0:
        Lmark = mark
    if mark > Hmark or i == 0:
        Hmark = mark
    avgMark = (avgMark * i + mark) / (i + 1)

print(f"The average of the marks is: {avgMark}")
print(f"The lowest mark is: {Lmark}")
print(f"The highest mark is: {Hmark}")