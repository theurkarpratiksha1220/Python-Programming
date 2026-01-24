# Write a program which accept N numbers from user and store it into list. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements: 13   5   45   7   4   56   34      
# Output :  56
# ----------------------------------------------------------------------------------------------------------------------
def Max(Arr):

    max_value = Arr[0]
    
    for i in range(len(Arr)):
        if Arr[i] > max_value:
            max_value = Arr[i]
    return max_value

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)     
        
    Ret = Max(Data)
    print("Maximum number is :", Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the number of elements : 7
# Enter the elements : 
# 13
# 5
# 45
# 7
# 4
# 56
# 34
# Maximum number is : 56