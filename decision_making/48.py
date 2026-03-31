'''"Question: Restaurant Bill Calculator
Calculate the total bill for dining at a restaurant:

Base meal cost is given as input
CGST: 2.5% and SGST: 2.5% (total GST = 5%)
Service charge: 10% if service is ""excellent"", 5% if ""good"", 0% if ""average""
If bill total > ₹2000: Apply 5% festival discount
If it's a weekend: Add ₹100 as weekend surcharge
If customer is senior citizen (60+): Give 10% discount on meal cost before tax

Take the values for meal_cost, service, day of week,
 age of person from user and then calculate the total bill as per the above criteria.
   Display the bill printing upto 2 decimal places only.

Sample Input: Meal = ₹1500, Service = ""good"", Day = ""weekend"", Age = 65
Expected Output: Total Bill: ₹1620.00"'''



age = int (input("enter your age: "))
day = str (input("enter day(weekday/weekend): "))
meal_cost = int (input("enter meal cost: "))
service = str (input("enter service(avg/good/excellent): "))
if age > 60:
    meal_cost = meal_cost - (0.1*meal_cost)
else:
    gst_bill = 0.05*meal_cost
    service_charge = 0 
    if (service == "good"):
        service_charge = 0.05*meal_cost
    elif(service =="excellent"):
        service_charge = 0.1*meal_cost
    bill = meal_cost + gst_bill + service_charge
    if (bill > 2000):
        bill = bill - (0.05*bill)
    if (day == "weekend"):
        bill += 100
    

print(f"your bill = {bill}")

