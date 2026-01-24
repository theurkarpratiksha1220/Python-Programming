# Write a program which contains one function that accept one number from user and
# returns true if number is divisible by 5 otherwise return false.
# Input : 8        Output : False
# Input : 25       Output : True
# ----------------------------------------------------------------------------------------------------------------------

def IdentifyNo(Value):

    if Value % 5 == 0:
        return True
    else:
        return False

def main():
    No = int(input("Enter any number : "))

    Ret = IdentifyNo(No)

    print(Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
#Enter any number : 8
#False

#Enter any number : 25
#True

#Enter any number : 30
#True

#Enter any number : 7
#False