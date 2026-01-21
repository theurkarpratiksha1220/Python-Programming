# Write a program which accepts one number and prints square of that number.
# Input: 5
# Output: 25
#-------------------------------------------------------------------------------------------------------

def SquareNo(Value):                             
    Ans = 0
    Ans = Value * Value
    return Ans

def main():
    No = 0
    Result = 0
                                            
    No = int(input("Enter Number : "))     

    Result = SquareNo(No)                     
    print(Result)

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
# Enter Number : 5
# 25
