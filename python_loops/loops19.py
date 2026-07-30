'''wap to take a no fro user and print its factorial
 if the user enters a -ve no, print "andha nki rey"'''

n = int(input("enter a number:"))
if n < 0:
    print("andha naki rey")

else:
    if n == 0:
        print(f"{n}! = 1")

    else:
        factorial =1 
        for i in range (1,n+1):
         factorial= factorial *1
         print(f"{n}! = {factorial}")

