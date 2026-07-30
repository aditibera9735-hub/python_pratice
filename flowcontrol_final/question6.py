'''Keep asking the user to enter words. Print each word.
 Stop asking and end the program if the user types "stop" (case-sensitive).'''

while True:
    word = input("enter a word(type stop to end):")
    print("your entered", word )

    if word == "stop":
        break
    print("end the program")


