'''"Question: Elish Maach Market Price Check
Write a program that takes the weight of a fish from the user.
At a fish market in Sealdah,
 elish maach costs ₹800/kg if weight > 1kg, otherwise ₹900/kg. Calculate total cost.

Expected Output Format:
Display price per kg and total cost"'''


weight = float(input("Enter weight of fish in kg: "))

if weight > 1:
    price_per_kg = 800
else:
    price_per_kg = 900

total_cost = weight * price_per_kg
print(f"Price per kg: ₹{price_per_kg}")
print(f"Total cost for {weight} kg: ₹{total_cost}")