# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934        
# Output :  37
# ----------------------------------------------------------------------------------------------------------------------

def SumDigits(Value):                                   
    Value = abs(Value)
    Sum = 0
    while Value > 0:
        Sum = Sum + Value % 10                 
        Value //= 10                              
    return Sum
           
def main():
    No = 0
                                               
    No = int(input("Enter Number : "))        
        
    Result = SumDigits(No)        
    print(Result)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Number : 5187934
# 37

# Enter Number : 12345
# 15