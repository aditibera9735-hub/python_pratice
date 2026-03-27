'''"Write a program that takes a person's age as input and determines 
if they are eligible to vote in West Bengal elections. If eligible, 
also check if they are a senior citizen (60+ years) for priority voting.
Expected Output Format:

If age < 18: ""Not eligible to vote""
If age 18-59: ""Eligible to vote""
If age >= 60: ""Eligible to vote with senior citizen priority"""'''


age=int(input("enter your age"))
if age < 18:
    print("not eligible to vote")
elif 18 <= age >= 59:
    print("eligible to vote")
elif age >= 60:
    print("eligible to vote with senior citizen priority")
else:
    print("vot dite hbe na")
