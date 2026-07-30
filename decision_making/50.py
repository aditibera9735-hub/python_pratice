'''Question: 
At Kolkata Book Fair, books under ₹200 get no discount, 
books ₹200-₹500 get 5% discount, books above ₹500 get 10% discount. 
Ask the user to input the book price.

Expected Output Format:
Display original price, discount amount, and final price of the book.'''

price = float(input("enter book price"))

if price >= 200:
    discount_percentage = 0 
elif price <= 500:
    discount_percentage = 5
else:
    discount_percentage = 10 

    discount_amount = price*(discount_percentage/100)
    final_price = price-discount_amount

    print(f"original price : {price}")
    print(f"discount({discount_percentage}%):{discount_amount}")
    print(f"final price :{final_price}")

