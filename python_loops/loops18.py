'''take 10 number from user and store it in a list print the number at odd index'''

mylist = 0 
for i in range(10):
    val = int(input(f"enter{i+1}number for list;"))
    mylist.append(val)
    for j in range(1,10,2):
        print(mylist[j])
