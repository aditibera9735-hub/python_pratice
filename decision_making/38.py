'''"Question: Sundarbans Safari Booking - 
Write a program for Sundarbans safari booking based on season and group size.

Input: Take season (string: ""winter"", ""summer"", ""monsoon"") and group size (integer) as input
Output: Print booking status and price per person

Logic:
If season is ""monsoon"": ""Booking closed due to monsoon""
Else:
    If winter and group size > 5: ₹2000 per person
    If winter and group size ≤ 5: ₹2500 per person
    If summer: ₹1500 per person (any group size)"'''


season = str(input("enter season:"))
group_size = int(input("enter group size"))
if season == "monsoon":
  print("booking close due to monsoon")
else:
     if season == "winter":
      if group_size > 5:
       price = 2000
      else:
        price = 2500

     else:
        if season == "summer":
         price = 1500
print(f"confirmed!price{price}")

    

