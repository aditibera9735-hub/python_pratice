''' take 10 numbers from the user and store it in a list.
 Print all the numbers at the even index places of the list using a while loop.'''

my_list = 0 
i =0 
while i<= 10:
    num = int(input(f"enter number{i+1}:"))
    my_list.append(num)
    i+=1
    j=0 
    while j in range (0,10,2):
        print(my_list[j])
        j+=2