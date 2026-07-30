''' Write a program to check tram service status based on weather and time.

Input: Take weather (string: ""clear"", ""rain"", ""storm"") and hour (0-23) as input
Output: Print service status

Logic:
If storm: ""Service suspended""
Else if rain:
    If hour between 6-22: ""Limited service""
    Else: ""No service""
Else (clear):
    If hour between 5-23: ""Full service""
    Else: ""No service"""

'''

Weather = input("enter weather(clear/rain/storm): ")
Time = int(input("enter time (0-23): "))
if  Weather == " storm ":
    status = "suspended"
elif Weather == "rain ":
    if 6 <= Time >= 22:
        status = "limited service"
    else:
        status = "no service"
else:
     if Weather == "clear ":
         5 <= Time >= 23
         status = " full service"
     else:
         status = "no service"

         print(f"tram service:{status}")
