'''"Help negotiate book prices at College Street based on book condition.
- New book: Pay marked price
- Like new: ""Ask for 10% discount""
- Good condition: ""Ask for 20% discount""
- Fair condition: ""Ask for 30% discount""
- Poor condition: ""Ask for 50% discount or look elsewhere"""'''


condition = str(input("enter book condition"))
if condition == "new":
  print("pay merket price")
elif condition == "good":
  print("ask for 20% discount")
elif condition == "fair":
  print("ask for 30% discount")
elif condition == "poor":
  print("ask for 50% discount")
else:
  print("look elsewhere")