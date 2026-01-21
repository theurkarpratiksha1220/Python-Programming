# Write a program which accepts one number and prints count of digits in that number
# Input: 7521
# Output: 4
#-------------------------------------------------------------------------------------------------------

def CountNo(Value):                               
    return len(str(abs(Value)))
           
def main():
    No = 0
                                       
    No = int(input("Enter Number : "))          
        
    Result = CountNo(No)                             
    print(Result)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
#Output
#Enter Number : 7521
#4

#Enter Number : 78954310
#8