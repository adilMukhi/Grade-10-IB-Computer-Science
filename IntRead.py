print("Give numbers: (Enter S to stop)")

numTrue = False
evenNum = 0
oddNum = 0

while numTrue == False:
    num = input()
    if num == "S":
       numTrue = True 
    else:
        num = int(num)
        if num % 2 == 0:
            evenNum += num
        elif num % 2 != 0:
            oddNum += num
        else:
            numTrue = True

print(f"Sum of all even numbers is {evenNum},\nand the sum of all odd numbers is {oddNum}")