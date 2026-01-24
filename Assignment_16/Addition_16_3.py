# Write a program which contains one function named as Add() which accepts two numbers from user 
# and return addition of that two numbers.
# Input : 11  5             Output : 16
# ----------------------------------------------------------------------------------------------------------------------

def Add():

    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Ret = No1 + No2

    print("Addition of two numbers is : ", Ret)

def main():
    Add()

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter First Number : 11
# Enter Second Number : 5
# Addition of two numbers is :  16