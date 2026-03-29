'''"Question: Kolkata Tram Service Status
Write a program to check tram service status based on weather and time.

Input: Take weather (string: ""clear"", ""rain"", ""storm"") and hour (0-23) as input
Output: Print service status
Logic:
If storm: ""Service suspended""
Else if rain:
    If hour between 6-22: ""Limited service""
    Else: ""No service""
Else (clear):
    If hour between 5-23: ""Full service""
    Else: ""No service"""'''

weather = (input('enter weather(clear/rain/storm) : '))
time = int(input("enter time(0-23) : "))
if weather == "storm":
    status = "sevice suspended"
elif weather == "rain":
    if 6 <= time <= 22:
        status = "limited service"
    else:
        status = "no service"
elif weather == "clear":
    if 5 <= time <= 23:
        status = "full service"
    else:
        status = "no service"

print(f"service status: {status}")