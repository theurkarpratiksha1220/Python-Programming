# Write a program which accept number from user and print that number of "*" on screen.
# Input : 5                Output :  *   *   *   *   *
# ----------------------------------------------------------------------------------------------------------------------

def DisplayPattern(Value):

    for i in range(Value):
        print("*", end="   ")
    print()

def main():
    No = int(input("Enter any number : "))

    Ret = DisplayPattern(No)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter any number : 5
# *   *   *   *   *   

# Enter any number : 3
# *   *   *   

# Enter any number : 2
# *   *   