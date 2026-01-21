# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.
#-------------------------------------------------------------------------------------------------------

def Addition(Value1, Value2):
    return Value1 + Value2

def Subtraction(Value1, Value2):
    return Value1 - Value2

def Multplication(Value1, Value2):
    return Value1 * Value2

def Division(Value1, Value2):
    if Value2 != 0:
        return Value1 / Value2
    else:
        return "Division by Zero."                       
           
def main():

    No1 = float(input("Enter First Number : "))
    No2 = float(input("Enter Second Number : "))
    
    Result1 = Addition(No1, No2)
    Result2 = Subtraction(No1,No2)
    Result3 = Multplication(No1,No2)
    Result4 = Division(No1,No2)

    print("Addition of numbers is : ", Result1)
    print("Subtraction of numbers is : ", Result2)
    print("Multiplication of numbers is : ", Result3)
    print("Division of numbers is : ", Result4)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter First Number : 2
#Enter Second Number : 3
#Addition of numbers is :  5.0
#Subtraction of numbers is :  -1.0
#Multiplication of numbers is :  6.0
#Division of numbers is :  0.6666666666666666

#Enter First Number : 0
#Enter Second Number : 1
#Addition of numbers is :  1.0
#Subtraction of numbers is :  -1.0
#Multiplication of numbers is :  0.0
#Division of numbers is :  0.0

#Enter First Number : 2
#Enter Second Number : 0
#Addition of numbers is :  2.0
#Subtraction of numbers is :  2.0
#Multiplication of numbers is :  0.0
#Division of numbers is :  Division by Zero.