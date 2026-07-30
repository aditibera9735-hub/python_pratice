'''Question: Write a program to check college admission eligibility.
 Minimum marks required is 75 for general category and 65 for reserved category.
Take input for marks and reservation category from user.
Expected Output Format:
Display eligibility status of candidate.'''

marks_percentage = float(input("enter your marks :"))
category = input("enter category(general/reserved): ").lower

if marks_percentage >=75:
   if category=="general":
    print("eligible for admission ")
   else:
        print("not eligibble")
elif  marks_percentage >=65:
   if category == "reserved":
      print("eligible for admission")
else:
   print("not eligible")




     
