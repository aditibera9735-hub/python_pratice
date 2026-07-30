'''take a number from user and store it into a list (sum of odd number - sum of even numbers )'''

my_list = []
for i in range(10):
    val = int(input("enter your number: "))
    my_list.append (val)
    even_sum = 0 
    for my_val in my_list:
        if (my_val% 2 == 0):
            even_sum += my_val
            odd_sum = 0 
            for my_val in my_list :
                if i%2 == 1:
                    odd_sum += my_val
print("odd_sum - even_sum")