# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12
#-------------------------------------------------------------------------------------------------------

def Factors(Value):
    Ans = []
    for i in range(1, Value+1):
        if Value % i == 0:
            Ans.append(i)
    return Ans                                    
           
def main():
    No = 0 
    No = int(input("Enter Any Number : "))
    
    if No <= 0:
        print("Invalid Input")
        return
    
    Result = Factors(No)

    for No in Result:                     
        print(No, end=" ")
    print() 

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Any Number : 12
#1 2 3 4 6 12 

#Enter Any Number : 3
#1 3 

#Enter Any Number : 21
#1 3 7 21 