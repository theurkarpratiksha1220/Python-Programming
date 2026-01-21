# Write a program which accepts one number and prints all odd numbers till that number.
#-------------------------------------------------------------------------------------------------------

def Odd(Value):                                
    Ans = []
    for i in range(1, Value+1):
        if i % 2 != 0:
            Ans.append(i)
    return Ans
                                 
def main():
    No = 0
                                           
    No = int(input("Enter Number : "))        
        
    Result = Odd(No)                         

    for No in Result:                            
        print(No, end=" ")
    print()

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 9
#1 3 5 7 9 

#Enter Number : 4
#1 3 