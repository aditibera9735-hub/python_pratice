''' PVR cinema charges different prices based on age, show timing, and membership status:
Children (age < 12): ₹150 for matinee, ₹200 for evening/night
Adults (12-59): ₹250 for matinee, ₹350 for evening/night
Senior Citizens (60+): ₹180 for matinee, ₹250 for evening/night
PVR Privilege members get 15% discount on all tickets
Students (age 13-25) get additional ₹50 off if they're not already members
Sample Input: Age = 22, Show = ""evening"", Member = ""no"", Student = ""yes""
Expected Output: Ticket Price: ₹300"'''


age = int(input("enter your age :"))
showtime =input("enter time (matinee/evening/night): ")
membership = input("do you have pvr membership(yes/no): ")

price = 0
if (5<= age < 12):
     if showtime == "matinee":
         price = 150
     elif  showtime == "evening" and showtime =="night":
          price = 200 
     else:
          print("invalid showtime")
elif  (12<= age < 59):
     if showtime == "matinee":
         price = 250
     elif  showtime == "evening" and showtime =="night":
          price = 350 
     else:
          print("invalid showtime")
else:
     if age == "60":
      if showtime == "matinee":
         price = 180
     elif  showtime == "evening" and showtime =="night":
          price = 250 
     else:
          print("invalid showtime")


if(membership == "yes"):
    price = 0.85*price

if ( 13 <= age >= 25 and membership =="no"):
     price -= 50 
    
     print(f" movie ticket price is {price}rupees")




         


          
     
