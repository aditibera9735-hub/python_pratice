'''"Question: SBI Home Loan Eligibility
State Bank of India approves home loans based on multiple criteria:

Age must be between 21-65
Monthly income ≥ ₹25,000
CIBIL score ≥ 700
Employment type: ""salaried"", ""self-employed"", or ""business""
If CIBIL score < 750, income must be ≥ ₹50,000
If age > 55, additional requirement: existing savings ≥ ₹5,00,000

Take values for age, monthly_income, CIBIL score, employment type, 
savings from user properly and print the loan status - approved/rejected as per the above criteria.


Sample Input: Age = 45, Income = 60000, CIBIL = 720, Employment = ""salaried"", Savings = 200000
Expected Output: Loan Status: Approved"'''



age = int(input("enter your age : "))
monthly_income = input("enter your incomr :")
cibil = int (input("enter cibil:"))
saving = input("enter saving:")
employment_type = str(input("enter employed type: "))

if 21 <= age <= 55:
    if (cibil < 750 and monthly_income >= 50000):
        loan_status = " approved"
elif age > 55:
    if saving >= 500000 and (cibil <750 and monthly_income >= 500000):
        loan_status = "approved"
else:
    loan_status = "rejected"

print(f" your loan request has been:{loan_status}")