# Write a program which accept N numbers from user and store it into list. Accept one another number from user
# and return frequency of that number from List
# Input : Number of elements : 11
# Input Elements: 13   5   45   7   4   56   5   34   2   5   65    
# Element to search : 5  
# Output :  3
# ----------------------------------------------------------------------------------------------------------------------
def FeqCount(Arr, Value):

    Count = 0
    
    for i in range(len(Arr)):
        if Arr[i] == Value:
            Count = Count + 1
    return Count

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     
        
    SearchNo = int(input("Element to search: "))

    Ret = FeqCount(Data, SearchNo)
    print("Count of number is :", Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the elements : 
# 13
# 5
# 45
# 7
# 4
# 56
# 5
# 34
# 2
# 5
# 65
# Element to search: 5
# Count of number is : 3