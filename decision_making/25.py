question'''"Create a calorie estimator for popular Bengali sweets.
- Rasgulla: 150 calories
- Sandesh: 120 calories
- Mishti Doi: 180 calories
- Chomchom: 200 calories
- If unknown sweet, show ""Calorie information not available"""'''





sweet = input("Enter  sweet name: ")
if sweet == rasgulla:
    print(" 150 calories")
elif sweet == sandesh:
    print(" 120 calories")
elif sweet == mishti doi:
    print(" 180 calories")
elif sweet == chomchom:
    print(" 200 calories")
else:
    print("Calorie information not available")