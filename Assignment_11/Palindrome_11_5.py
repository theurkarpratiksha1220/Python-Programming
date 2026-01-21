# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome
#-------------------------------------------------------------------------------------------------------

def PalindromeNo(Value):                                    
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
    Result = PalindromeNo(No)                          

    if No == Result:
        print("Palindrome")
    else:
        print("No Palindrome")

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 121
#Palindrome

#Enter Number : -121 
#Palindrome

#Enter Number : 1223
#No Palindrome

#Enter Number : -1223
#No Palindrome