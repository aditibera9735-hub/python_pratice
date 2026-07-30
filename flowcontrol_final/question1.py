'''Ask the user to enter an integer. Determine if the number is even or odd and print the result.'''

num_str = input("enter an integer: ")
num = int(num_str)
if num %2 == 0:
    print("even number")
else:
    print("odd number")
