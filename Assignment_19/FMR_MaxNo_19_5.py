# Write a program which contains filter(), map(), reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers.
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.
# (You can also use normal function instead of lambda functions)

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62
# ----------------------------------------------------------------------------------------------------------------------

from functools import reduce

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    No = int(input("Enter numbers you want in list : "))

    Data = []
    for i in range(No):
        Value = int(input("Enter numbers of list : "))
        Data.append(Value)
        
    print("Actual Data is :",Data)

    FData = list(filter(ChkPrime, Data))
    print("Data after filter is :",FData)

    MData = list(map(lambda No : No * 2,FData))
    print("Data after map is : ",MData)
    
    RData = reduce((lambda A,B : A if A > B else B), MData)
    print("Data after reduce is :", RData)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter numbers you want in list : 8
# Enter numbers of list : 2
# Enter numbers of list : 70
# Enter numbers of list : 11
# Enter numbers of list : 10
# Enter numbers of list : 17
# Enter numbers of list : 23
# Enter numbers of list : 31
# Enter numbers of list : 77
# Actual Data is : [2, 70, 11, 10, 17, 23, 31, 77]
# Data after filter is : [2, 11, 17, 23, 31]
# Data after map is :  [4, 22, 34, 46, 62]
# Data after reduce is : 62