# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4   3           Output :  12
# Input : 6   3           Output :  18
# ----------------------------------------------------------------------------------------------------------------------

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

Multiplication = lambda No1, No2 : No1 * No2

Ret = Multiplication(No1, No2)

print("Multiplication of two numbers is : ",Ret)

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter First Number : 4
# Enter Second Number : 3
# Multiplication of two numbers is :  12

# Enter First Number : 6
# Enter Second Number : 3
# Multiplication of two numbers is :  18