'''"""Question: Bengali Sweet Shop Discount
A sweet shop offers 10% discount if purchase is above ₹500.
 Write a program to ask the user for the purchase amount and then calculate final amount after discount.

Expected Output Format:
Display original amount, discount, and final amount"""'''


amount = float(input("Enter purchase amount: ₹"))

if amount > 500:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"Original amount: ₹{amount}")
    print(f"Discount (10%): ₹{discount}")
    print(f"Final amount: ₹{final_amount}")
else:
    print(f"No discount applicable. Amount to pay: ₹{amount}")