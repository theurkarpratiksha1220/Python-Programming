# Write a lambda function which accepts two numbers and returns multiplication
#------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

MultiplicationNo = lambda No1, No2 : No1 * No2

Ret = MultiplicationNo(No1, No2)

print("Multiplication of two numbers is : ",Ret)

#------------------------------------------------------------------------
# Output -
#Enter First Number : 3
#Enter Second Number : 4
#Multiplication of two numbers is :  12

#Enter First Number : 0
#Enter Second Number : 12
#Multiplication of two numbers is :  0