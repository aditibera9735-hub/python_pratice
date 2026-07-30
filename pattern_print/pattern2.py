'''5 4 3 2 1
   5 4 3 2
   5 4 3
   5 4
   5'''

rows = 5
for i in range(rows , 0,-1):
    for j in range(rows , i-1 ,-1):
        print(j,end="")
    print()