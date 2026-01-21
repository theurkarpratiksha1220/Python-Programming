# Write a program which accepts one number and prints that many numbers in reverse order
# Input: 5
# Output: 5 4 3 2 1
#-------------------------------------------------------------------------------------------------------

def DisplaySeries(Value):                                      
    Value = abs(Value)
    ReverseValues = []

    for i in range(Value, 0, -1):
        ReverseValues.append(i)  
 
    return ReverseValues

def main():
    No = 0

    No = int(input("Enter Any Number : "))                   
    Result = DisplaySeries(No)                            

    for No in Result:
        print(No, end=" ")
    print()

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter Any Number : 5
#5 4 3 2 1 
