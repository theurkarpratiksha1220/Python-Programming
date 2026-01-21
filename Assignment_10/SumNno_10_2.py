# Write a program which accepts one number and prints sum of first N natural numbers
# Input: 5
# Output: 15
#-------------------------------------------------------------------------------------------------------

def SumNno(Value):                                
    Ans = 0
    for i in range(1, Value+1):
        Ans = Ans + i
    return Ans
                                 
def main():
    No = 0
    Result = 0
                                        
    No = int(input("Enter Number : "))            

    Result = SumNno(No)                        
    print(Result)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 5
#15

#Enter Number : 8
#36
