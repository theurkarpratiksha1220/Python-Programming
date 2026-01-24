# Write a program which accept one number from user and return its factorial.
# Input : 5         Output :  120
# ----------------------------------------------------------------------------------------------------------------------

def Fact(Value):                                   
    Ans = 1
    for i in range(1, Value+1):
        Ans = Ans * i
    return Ans
                                 
def main():
    No = 0
    Result = 0
                                              
    No = int(input("Enter Number : "))           

    if No < 0:
        print("Negative values not accepted")
        return
        
    Result = Fact(No)                   
    print(Result)

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 5
#120

#Enter Number : 0
#1
