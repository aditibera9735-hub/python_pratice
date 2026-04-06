'''"Count the number of digits in a given number.
Example: 1234 → 4 digits"'''

count = 0 
n = 1234
while n>0 :
    n = n//10
    count += 1
    print(count)