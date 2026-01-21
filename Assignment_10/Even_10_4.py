# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10
#-------------------------------------------------------------------------------------------------------

def Even(Value):                                  
    Ans = []
    for i in range(2, Value+1):
        if i % 2 == 0:
            Ans.append(i)
    return Ans
                                 
def main():
    No = 0
                                           
    No = int(input("Enter Number : "))           
        
    Result = Even(No)                         

    for No in Result:                    
        print(No, end=" ")
    print()

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 10
#2 4 6 8 10 

#Enter Number : 5
#2 4 