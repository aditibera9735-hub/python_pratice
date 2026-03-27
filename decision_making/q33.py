'''"Question: College Admission Eligibility - 
Write a program to check college admission eligibility. 
Minimum marks required is 75% for general category and 65% for reserved category.
Take input for marks and reservation category from user.
Expected Output Format:
Display eligibility status of candidate."'''


marks_percentage = float(input("Enter marks percentage: "))
category = input("Enter category (general/reserved): ")

if category == "general":
    if marks_percentage >= 75:
        print("Eligible for admission")
    else:
        print("Not eligible for admission")
elif category == "reserved":
    if marks_percentage >= 65:
        print("Eligible for admission")
    else:
        print("Not eligible for admission")
else:
    print("Invalid category")
