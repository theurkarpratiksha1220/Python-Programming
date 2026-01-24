# Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even.
# Map function will calculate its square. Reduce will return addition of all that numbers

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
# ----------------------------------------------------------------------------------------------------------------------

from functools import reduce

def main():
    No = int(input("Enter numbers you want in list : "))

    Data = []
    for i in range(No):
        Value = int(input("Enter numbers of list : "))
        Data.append(Value)
        
    print("Actual Data is :",Data)

    FData = list(filter((lambda No : No % 2 == 0), Data))
    print("Data after filter is :",FData)

    MData = list(map(lambda No : No ** 2,FData))
    print("Data after map is : ",MData)
    
    RData = reduce((lambda No1,No2 : No1 + No2), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter numbers you want in list : 10
# Enter numbers of list : 5
# Enter numbers of list : 2
# Enter numbers of list : 3
# Enter numbers of list : 4
# Enter numbers of list : 3
# Enter numbers of list : 4
# Enter numbers of list : 1
# Enter numbers of list : 2
# Enter numbers of list : 8
# Enter numbers of list : 10
# Actual Data is : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# Data after filter is : [2, 4, 4, 2, 8, 10]
# Data after map is :  [4, 16, 16, 4, 64, 100]
# Data after reduce is : 204