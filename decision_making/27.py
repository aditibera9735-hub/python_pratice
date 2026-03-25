'''question"Suggest best travel times to cross Howrah Bridge based on traffic patterns.
- 5 AM to 7 AM: ""Light traffic - smooth journey""
- 8 AM to 11 AM: ""Heavy traffic - expect delays""
- 12 PM to 4 PM: ""Moderate traffic - reasonable time""
- 5 PM to 9 PM: ""Peak traffic - consider alternate route""
- 10 PM to 4 AM: ""Very light traffic - fastest route"""'''


times=int(input("enter time 24hr format"))
if 5 <= times >= 7:
    print("light traffic - smooth journey")
elif 8 <= times >= 11:
    print("heavy traffic - expect delays")
elif 12 <= times >= 4:
    print("moderate traffic - reasonable time")
elif 5 <= times >= 9:
    print("peak traffic - consider alternate route")
elif 10 <= times >= 4:
    print("very light traffic - fastest route")
else:
    print("invalid time")