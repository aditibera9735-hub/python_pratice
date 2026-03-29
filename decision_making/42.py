'''"Question: Poila Boishakh Celebration Venue -   
Write a program to suggest Poila Boishakh celebration venue based on budget and group size.

Input: Take budget (integer) and group size (integer) as input
Output: Print suggested venue

Logic:
If budget > 10000:
    If group size > 50: ""Book a community hall""
    Else: ""Celebrate at a restaurant""

Else:
    If group size > 20: ""Organize at local park""
    Else: ""Celebrate at home"""'''


budget = int(input("enter your budget:" ))
group_size = int (input("enter group_size:" ))
if budget >= 1000:
    if group_size >= 50:
        venue =" book a community hall"

    else:
        venue = "celebrate at a resturant"
else:
    if group_size >= 20:
        venue = "organize at local park"

    else:
        venue = "celebrate at home"

print(f"suggested :{venue }")


