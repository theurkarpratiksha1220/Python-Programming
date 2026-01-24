# Write a program which accept one number from user and return addition of its factors.
# Input : 12         Output :  16     (1+2+3+4+6)
# ----------------------------------------------------------------------------------------------------------------------

def SumFactors(Value):
    Sum = 0

    for i in range(1, Value):
        if Value % i == 0:
            Sum = Sum + i 
    return Sum


def main():

    No = int(input("Enter Number : "))

    if No <= 0:
        print("Please enter valid positive number")
        return
    
    Ret = SumFactors(No)
    print(Ret)


if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Number : 12
# 16

# Enter Number : 5
# 1

# Enter Number : 10
# 8