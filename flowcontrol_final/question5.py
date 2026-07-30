'''Ask the user to enter 5 numbers one by one.
 Store only the positive numbers in a list. After collecting all inputs,
   print the list of positive numbers.'''

positive_number = []
count =0 
num_str = input("enter number :(count+1)")
num = int(num_str)
if num>0:
    positive_number.append(num)
    count = count+1

    print(f"positive number entered:",positive_number )