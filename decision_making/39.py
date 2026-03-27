'''"Question : Kali Puja Fireworks Permission -
Write a program to check fireworks permission during Kali Puja based on location and time.

Input: Take location (string: ""residential"" or ""commercial"") and hour (0-23) as input
Output: Print ""Allowed"" or ""Not Allowed""

Logic:
If residential area:
    If time between 18-22: Allowed
    Else: Not Allowed

If commercial area:
    If time between 16-23: Allowed
    Else: Not Allowed"'''


time = int(input("enter time hr(0-23):"))
area = (input("enter area (residential/commercial)"))
if area == "residential":
    if 18 <= time >= 22:
        print("allowed")

    else:
        print("not allowed")

        if area == "commercial":
            if 16 <= time >= 23:
                print("allowed")
            else:
                print("not allowed")

else:
    print(f"fireworks:{allowed}")
