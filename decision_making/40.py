'''"Question : Elish Maach Market Price - 
Write a program to determine elish maach price based on size and season.

Input: Take fish size (string: ""small"", ""medium"", ""large"") and season (string: ""monsoon"" or ""other"") as input
Output: Print price per kg

Logic:
If monsoon season: Small: ₹800/kg, Medium: ₹1000/kg, Large: ₹1200/kg
If other season: Small: ₹1200/kg, Medium: ₹1500/kg, Large: ₹1800/kg"'''

size = input("enter fish size(small/medium/large):")
season = input("enter season9(monsoon/other):")
if season == "monsoon":
    if size == "small":
        price = 800

    elif size == "medium":
         price = 1000
    else:
        size == "large"
        price = 1200

else:
    if season == "other":
        if size == "small":
            price = 1200
    elif size == "medium":
        price = 1500
    else:
        if size == "large":
            price = 1800

print(f"llish price: {price}in kg")


         


