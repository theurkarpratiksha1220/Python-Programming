# Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11        Output : Positive number
# Input : -8        Output : Negative number
# Input : 0         Output : Zero
# ----------------------------------------------------------------------------------------------------------------------

def IdentifyNo(Value):
    if Value > 0:
        return "Positive Number"
    elif Value < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():

    No = int(input("Enter any number : "))

    Ret = IdentifyNo(No)

    print(Ret)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
#Enter any number : 11
#Positive Number

#Enter any number : -8
#Negative Number

#Enter any number : 0
#Zero