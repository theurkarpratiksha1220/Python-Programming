# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6
#-------------------------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------------------------------------
#Output
#Enter Number : 123
#6
