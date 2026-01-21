# Write a program which accepts one number and prints that many numbers starting from 1
# Input: 5
# Output: 1 2 3 4 5
#-------------------------------------------------------------------------------------------------------

def DisplaySeries(Value):                                      
    Value = abs(Value)
    PrintValues = []

    for i in range(1, Value+1):
        PrintValues.append(i)  
 
    return PrintValues

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
#1 2 3 4 5 

#Enter Any Number : 10
#1 2 3 4 5 6 7 8 9 10 
