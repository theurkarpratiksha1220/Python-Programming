# Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than
# or equal to 70 and less than or equal to 90. map function will increase each number by 10. Reduce will return product
# of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
# ----------------------------------------------------------------------------------------------------------------------

from functools import reduce

def main():
    No = int(input("Enter numbers you want in list : "))

    Data = []
    for i in range(No):
        Value = int(input("Enter numbers of list : "))
        Data.append(Value)
        
    print("Actual Data is :",Data)

    FData = list(filter((lambda No : No >= 70 and No <= 90), Data))
    print("Data after filter is :",FData)

    MData = list(map(lambda No : No + 10,FData))
    print("Data after map is : ",MData)
    
    RData = reduce((lambda A,B : A * B), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter numbers you want in list : 12
# Enter numbers of list : 4
# Enter numbers of list : 34
# Enter numbers of list : 36
# Enter numbers of list : 76
# Enter numbers of list : 68
# Enter numbers of list : 24
# Enter numbers of list : 89
# Enter numbers of list : 23
# Enter numbers of list : 86
# Enter numbers of list : 90
# Enter numbers of list : 45
# Enter numbers of list : 70
# Actual Data is : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# Data after filter is : [76, 89, 86, 90, 70]
# Data after map is :  [86, 99, 96, 100, 80]
# Data after reduce is : 6538752000