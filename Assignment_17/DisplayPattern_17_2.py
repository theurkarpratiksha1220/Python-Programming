# Write a program which accept one number and display below pattern.
# Input : 5
# Output :  *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
# ----------------------------------------------------------------------------------------------------------------------

def DisplayPattern(Value):
    for i in range(Value):
        for j in range(Value):
            print("*", end="  ")
        print()

def main():
    No = 0
    
    No = int(input("Enter Number : "))

    DisplayPattern(No)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -

# Enter Number : 5
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  *  

# Enter Number : 3
# *  *  *  
# *  *  *  
# *  *  *  

# Enter Number : 2
# *  *  
# *  *  