# Write a program which accepts one number and prints reverse of that number
# Input: 123
# Output: 321
#-------------------------------------------------------------------------------------------------------

def ReverseDigits(Value):                                   
    NegValue = Value < 0
    Value = abs(Value)
    Reverse = 0

    while Value > 0:
        Reverse = Reverse * 10 + Value % 10               
        Value //= 10   
        
    if NegValue:
         return -Reverse
    else:
        return Reverse                                      
           
def main():
    No = 0
                                                  
    No = int(input("Enter Number : "))                    
    Result = ReverseDigits(No)                          

    print(Result)
    
if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
# Enter Number : 123
# 321

# Enter Number : -123
# -321