# Write a program which accept N numbers from user and store it into list. Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements: 13   5   45   7    
# Output :  5
# ----------------------------------------------------------------------------------------------------------------------
def Minimum(Arr):

    min_value = Arr[0]
    
    for i in range(len(Arr)):
        if Arr[i] < min_value:
            min_value = Arr[i]
    return min_value

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     
        
    Ret = Minimum(Data)
    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the number of elements : 4
# Enter the elements : 
# 13
# 5
# 45
# 7
# Maximum number is : 5