''' Write a program to suggest Poila Boishakh celebration venue based on budget and group size.

Input: Take budget (integer) and group size (integer) as input
Output: Print suggested venue

Logic:
If budget > 10000:
    If group size > 50: ""Book a community hall""
    Else: ""Celebrate at a restaurant""

Else:
    If group size > 20: ""Organize at local park""
    Else: ""Celebrate at home"""
'''

budget = int(input("enter your budget: "))
group_size = int(input("enter your group size :"))
 
if budget >= 10000:
   if group_size == 50 :
    venu = "book community hall"
   else:
     venu = "celebrate at a restaurant"

else:
  if group_size == 20:
    venu = "organize at local park"
  else:
    venu = "celebrate at home"

    print(f"suggested venu:{venu}")
#budget = int(input("Enter your budget: "))
group_size = int(input("Enter group size: "))

if budget > 10000:
    if group_size > 50:
        venue = "Book a community hall"
    else:
        venue = "Celebrate at a restaurant"
else:
    if group_size > 20:
        venue = "Organize at local park"
    else:
        venue = "Celebrate at home"

print(f"Suggestion: {venue}")

budget = int(input("Enter your budget: "))
group_size = int(input("Enter group size: "))

if budget > 10000:
    if group_size > 50:
        venue = "Book a community hall"
    else:
        venue = "Celebrate at a restaurant"
else:
    if group_size > 20:
        venue = "Organize at local park"
    else:
        venue = "Celebrate at home"

print(f"Suggestion: {venue}")