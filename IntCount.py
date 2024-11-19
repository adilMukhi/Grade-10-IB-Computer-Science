posNum = 0
negNum = 0
zeroNum = 0
stop = False

print("Enter a series of numbers (enter S to stop):")

while not stop:
    num = input()
    if num == "S":
        stop = True
    else:
        num = int(num)
        if num > 0:
            posNum += 1
        elif num < 0:
            negNum += 1
        elif num == 0:
            zeroNum += 1
        else:
            print("Invalid input. Please enter a number or 'S' to stop.")

print("Positive numbers:", posNum)
print("Negative numbers:", negNum)
print("Zeroes:", zeroNum)