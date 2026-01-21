# Write a program which accepts one number and prints multiplication table of that number
# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40
#-------------------------------------------------------------------------------------------------------

def MultTable(Value):                                 
    Ans = []
    for i in range(1, 11):
        Ans.append(Value * i)
    return Ans
                                 
def main():
    No = 0
                                         
    No = int(input("Enter Number : "))            

    Result = MultTable(No)                     
                                                        
    for No in Result:                 
        print(No, end=" ")
    print()

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------
# Output
#Enter Number : 4
#4 8 12 16 20 24 28 32 36 40 

#Enter Number : 10
#10 20 30 40 50 60 70 80 90 100 
