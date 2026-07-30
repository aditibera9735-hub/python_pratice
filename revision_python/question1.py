'''
Question 1 : Write a program to check fireworks permission
during Kali Puja based on location and time.

Input: Take location (string: ""residential"" or ""commercial"")
 and hour (0-23) as input
Output: Print ""Allowed"" or ""Not Allowed""

Logic:
If residential area:
    If time between 18-22: Allowed
    Else: Not Allowed

If commercial area:
    If time between 16-23: Allowed
    Else: Not Allowed"


'''


area = str(input("enter your location(residential/commercial): "))
hours = int(input("enter hours(0-23) :"))
if area == "residential ":
   if  18 <= hours >= 22:
    permision = " not allowed "
   else:
     permission = " allowed "

else:
  if 16 <= hours >= 23:
    permision = " not allowed "
  else:
    permission = " allowed "

    print(F"fireworks: {permission} ")


