'''approach - 2 '''

n = int(input("enter a number : "))
countdivisors = 0 
for i in range (1,n+1):
    if (n%i == 0 ):
        countdivisor +=1
if (countdivisors == 2):
    print("its a prime no")
else:
    print("not prime no")
