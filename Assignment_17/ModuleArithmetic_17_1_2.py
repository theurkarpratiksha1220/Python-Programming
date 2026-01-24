# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
# Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform
# the operation. Write on python program which call all the functions from Arithmetic module by accepting 
# the parameters from user.
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------- Uses Arithmetic Module-------------------------------------------------------
import Arithmetic_17_1_1

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("Addition is :", Arithmetic_17_1_1.Add(Value1, Value2))
    print("Subtraction is :", Arithmetic_17_1_1.Sub(Value1, Value2))
    print("Multiplication is :", Arithmetic_17_1_1.Mult(Value1, Value2))
    print("Division is :", Arithmetic_17_1_1.Div(Value1, Value2))


if __name__ == "__main__":
    main()


# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter first number : 11
# Enter second number : 10
# Addition is : 21
# Subtraction is : 1
# Multiplication is : 110
# Division is : 1.1