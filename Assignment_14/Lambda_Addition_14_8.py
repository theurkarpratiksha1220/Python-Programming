# Write a lambda function which accepts two numbers and returns addition
#------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

Add = lambda No1, No2 : No1 + No2

Ret = Add(No1,No2)

print("Addition is : ",Ret)

#------------------------------------------------------------------------
# Output -
#Enter First Number : 3
#Enter Second Number : 8
#Addition is :  11