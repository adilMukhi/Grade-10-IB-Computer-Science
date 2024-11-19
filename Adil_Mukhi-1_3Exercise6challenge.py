# Adil Mukhi - Sep 24, 2024
# 1.3 Input 6. Exercise1.5challenge

"""
Create a program that calculates the percentage you earned on a test given that
each section of a test is worth 20 marks (for a total of 80 marks) and that the weight of each section is
as follows:
"""


# My Work:
KuPercent = 0.25
ThPercent = 0.25
ComPercent = 0.2
ApliPercent = 0.3

print("------------------------------------------------------")
kuMarks = float(input("KNOWLEDGE AND UNDERSTANDING		="))
ThMarks = float(input("THINKING				="))
ComMarks = float(input("COMMUNICATION				="))
ApliMarks = float(input("APPLICATION				="))
print("------------------------------------------------------")
totalMarks = (kuMarks * KuPercent) + (ThMarks * ThPercent) + (ComMarks * ComPercent) + (ApliMarks * ApliPercent)
print ("TOTAL MARKS EARNED:		", (kuMarks + ThMarks + ComMarks + ApliMarks), "/80")

totalPercent = totalMarks * 5
print ("TOTAL PERCENTAGE EARNED		", totalPercent)



"""
# ARAHGYA'S WORK:

#Arghya Vyas
'''
Create a program that calculates the percentage you earned on a test given that
each section of a test is worth 20 marks (for a total of 80 marks) and that the weight of each section is
as follows:
KNOWLEDGE AND UNDERSTANDING = 25%
THINKING = 25%
COMMUNICATION = 20%
APPLICATION = 30%
'''

knowledgeAndUnderstanding = float(input("Enter the marks for Knowledge and Understanding (out of 20): "))
thinking = float(input("Enter the marks for Thinking (out of 20): "))
communication = float(input("Enter the marks for Communication (out of 20): "))
application = float(input("Enter the marks for Application (out of 20): "))

totalMarks = (knowledgeAndUnderstanding * 0.25) + (thinking * 0.25) + (communication * 0.2) + (application * 0.3)
percentage = totalMarks * (100 / 20)

print(f"Total Marks: {knowledgeAndUnderstanding + thinking + communication + application} /80")
print(f"Overall Percentage: {percentage:.2f}%")

"""