# Write a program which accept N numbers from user and store it into list. Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements: 13   5   45   7   4   56        
# Output :  130
# ----------------------------------------------------------------------------------------------------------------------
def Summation(Arr):
    Sum = 0 
    
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     
        
    Ret = Summation(Data)
    print("Summation is :", Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the number of elements : 6
# Enter the elements : 
# 13
# 5
# 45
# 7
# 4
# 56
# Summation is : 130