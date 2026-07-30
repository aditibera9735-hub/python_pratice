'''take 3 numbers from user and store them in 3 different variables.
 add the 3 numbers and store it in a variables "temp " .
   now take "temp" numbers from user and store it in a list '''

a,b,c = map(int(input("enter 3 number :").split()))
temp = a+b+c 
mylist = []
for i in range (temp):
    val = int(input(f"enter {i+1}number for the list :"))
    mylist.append(val)
print(f"my list looks like this : {mylist}")