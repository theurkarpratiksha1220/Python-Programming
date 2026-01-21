# Write a lambda function which accepts two numbers and returns maximum number.
#------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

MaxNumber = lambda No1, No2 : No1 if No1 > No2 else No2

Ret = MaxNumber(No1,No2)

print("Maximum Number is : ",Ret)

#------------------------------------------------------------------------
# Output -
#Enter First Number : 12
#Enter Second Number : 13
#Maximum Number is :  13

#Enter First Number : 114
#Enter Second Number : 12
#Maximum Number is :  114