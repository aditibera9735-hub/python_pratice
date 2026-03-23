question'''"Ask the user to enter a movie rating out of 5 and provide a message based on the following conditions - 
5.0: ""Bhai masterpiece dekh liya 🔥""
4.0 to 4.9: ""Bhai badiya movie thi 👌""
3.0 to 3.9: ""Theek thaak thi, timepass 😐""
2.0 to 2.9: ""Meh! Bore ho gaya yaar 😴""
Below 2.0: ""Mat dekhna bhai, time barbaad 🚫"""'''



rating=float(input("enter movie rating"))
if rating == 5.0:
    print("bhai masterpiece dekh liya")

elif 4.0 < rating > 5.0:
    print("bhai badiya movie thi")

elif 3.0 < rating > 3.9:
    print("theek thaak thi , timepass")

elif 2.0 < rating > 2.9:
    print("meh! bore ho gaya yaar")
elif rating < 2.0:
    print("mat dekhna bhai, time barbad")
else:
    print("chol momo kheye asi")
    