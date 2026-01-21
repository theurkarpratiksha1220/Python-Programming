# Write a lambda function which accepts two numbers and returns minimum number.
#------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

MinNumber = lambda No1, No2 : No1 if No1 < No2 else No2

Ret = MinNumber(No1,No2)

print("Minimum Number is : ",Ret)

#------------------------------------------------------------------------
# Output -
#Enter First Number : 12
#Enter Second Number : 13
#Minimum Number is :  12

#Enter First Number : 114
#Enter Second Number : 12
#Minimum Number is :  12