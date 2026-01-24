# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934        
# Output :  7
# ----------------------------------------------------------------------------------------------------------------------

def CountNo(Value):                               
    return len(str(abs(Value)))
           
def main():
    No = 0
                                       
    No = int(input("Enter Number : "))          
        
    Result = CountNo(No)                             
    print(Result)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Number : 5187934
# 7

# Enter Number : 12345
# 5