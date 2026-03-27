'''"Question : Kolkata Metro Line Fare Calculator - 
Write a program to calculate metro fare in Kolkata based on the number of stations traveled.

Input: Take the number of stations as input from the user
Output: Print the fare amount

Logic:
If stations ≤ 5: fare is ₹10
If stations > 5 and ≤ 10: fare is ₹15
If stations > 10: fare is ₹20"'''


station=int(input("enter  number of station"))
if station <= 5:
    fare = 10
else:
     5 < station <= 10
     fare = 15
    else:
    fare = 20
print(F"metro fare{fare}")
