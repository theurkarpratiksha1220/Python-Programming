# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input: 10 20
# Output: 20 is greater
#-------------------------------------------------------------------------------------------------------

def ChkGreater(Value1, Value2):   
    if Value1 > Value2:
        return Value1
    else:
        return Value2

def main():
    No1 = 0
    No2 = 0
    Result = 0
                                             
    No1 = int(input("Enter first number : "))      
    No2 = int(input("Enter second number : "))    

    Result = ChkGreater(No1, No2)               
    print(Result, "is greater")

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output -
# Enter first number : 10
# Enter second number : 20
# 20 is greater