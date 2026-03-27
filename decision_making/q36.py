'''"Question: Howrah Bridge Traffic Status - 
Write a program to determine traffic status on Howrah Bridge based on time and vehicle count.

Input: Take hour (0-23) and vehicle count as input.
Output: Print traffic status: ""Light"", ""Moderate"", or ""Heavy""
Logic:
If hour is between 7-10 or 17-20 (rush hours) -> if vehicles are greater than 500, then traffic status is ""Heavy"", else it is ""Moderate""
If it is (non-rush hours) and the vehicles count is greater than 300, then traffic status is ""Moderate"", else it is ""Light""

Note - Refer the solution if you can't understand the question."'''

hour = int(input("enter hour(0-23):"))

vehicles = int(input("enter vehicles count:"))

if 7 <= hour >= 10 or 17<= hour >= 20:
   
   if vehicles  >= 500:
      
      status = "heavy"
else:
    status ="moderate"

    if 10<= hour >= 16 or 21 <= hour >= 9:
      
      if vehicles >= 300:
         
         status ="moderate"
    else:
         status ="light"

print(f"traffic status: {status}")
 