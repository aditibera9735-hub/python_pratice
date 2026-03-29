'''"Question: Book Fair Discount
At Kolkata Book Fair, books under ₹200 get no discount,
 books ₹200-₹500 get 5% discount, books above ₹500 get 10% discount. Ask the user to input the book price.

Expected Output Format:
Display original price, discount amount, and final price of the book."'''

price = int(input("enter your price:"))

if price <= 200:
    discount  = 0 
elif price <= 500:
    discount = 5 
else:
    discount = 10 
discount_price = price * (discount/price)
final_price = price - discount 
print(f"original price:{price}")
print(f"discount:{discount}%")
print(f"final price:{final_price}")

    

