'''question "Suggest appropriate clothing for Kolkata weather.
- Temperature > 35°C: ""Wear light cotton clothes and carry water""
- Temperature 25-35°C: ""Comfortable weather - normal clothes""
- Temperature 15-24°C: ""Pleasant weather - light jacket recommended""
- Temperature < 15°C: ""Cold weather - wear warm clothes"""'''


temperature = int(input("appropriate clothing for kolkata weather"))
if temperature >= 35 :
    print("wear light cotton clothes and carry water")
elif  25 <= temperature >=  35:
    print("comfortable weather - normal clothes")
elif 15 <= temperature >= 24:
    print("pleasant weather - light jackest recommended")
elif  temperature <= 15:
    print("cold weather - wear warm clothes")
