# Write a lambda function which accepts three numbers and returns largest number.
#------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))
No3 = int(input("Enter Third Number : "))

LargestNo = lambda No1, No2, No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

Ret = LargestNo(No1,No2,No3)

print("Largest Number is : ", Ret)

#------------------------------------------------------------------------
# Output -
#Enter First Number : 2
#Enter Second Number : 3
#Enter Third Number : 3
#Largest Number is :  3

#Enter First Number : 5
#Enter Second Number : 6
#Enter Third Number : 7
#Largest Number is :  7