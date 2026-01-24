# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4             Output :  16
# Input : 6             Output :  64
# ----------------------------------------------------------------------------------------------------------------------

No = int(input("Enter Any Number : "))

PowerofTwo = lambda No : 2 ** No

Ret = PowerofTwo(No)

print("Power of two of a number is : ",Ret)

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Any Number : 4
# Power of two of a number is :  16

# Enter Any Number : 6
# Power of two of a number is :  64