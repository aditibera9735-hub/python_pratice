'''"Suggest which compartment to board based on passenger type.
- Age < 18: ""General compartment or ask adult for help""
- Age 18-59 and gender is ""female"": ""Ladies compartment available""
- Age 18-59 and gender is ""male"": ""General compartment""
- Age >= 60: ""Senior citizen compartment (if available) or general"""'''


age= int(input("enter your age"))
if age <= 18:
    print("general compartment or ask adult for help")
elif 18 <= age >= 59, gender == female:
    print( "ladies comartment available")
elif 18 <= age >= 59, gender == male:
    print("general compartment")
elif age >= 60:
    print("senior citizen compartment ")
else:
    print("general compartment")