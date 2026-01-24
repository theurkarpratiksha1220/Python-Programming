# Write a program which accept N numbers from user and store it into list. Return addition of all prime numbers from that list.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user 
# defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
#
# Input : Number of elements : 11
# Input Elements: 13   5   45   7   4   56   10   34   2   5   8    
# Output :  32 (13+5+7+2+5)
# ----------------------------------------- Main File -----------------------------------------------------------------------

import MarvellousNum_18_5

def ListPrime(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if MarvellousNum_18_5.ChkPrime(Arr[i]):
            Sum = Sum + Arr[i]

    return Sum


def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print("Addition of prime numbers is :", Ret)


if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------------------------------------------
# Output:
# Enter the number of elements : 11
# Enter the elements : 
# 13
# 5
# 45
# 7
# 4
# 56
# 10
# 34
# 2
# 5
# 8
# Addition of prime numbers is : 32