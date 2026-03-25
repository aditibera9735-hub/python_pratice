'''question "Help negotiate fish prices at local markets based on quantity.
- 1 kg: Pay full price
- 2-4 kg: ""Ask for 5% discount""
- 5-9 kg: ""Ask for 10% discount""
- 10+ kg: ""Ask for 15% discount and free cleaning"""'''


quantity=float(input("enter fish quantity"))
if quantity == 1:
    print("pay full price")
elif 2 < quantity > 4:
    print("ask 5% discount")
elif 5 < quantity > 9:
    print("ask for 10% discount")
elif quantity <=10:
    print("15% discount and free cleaning")