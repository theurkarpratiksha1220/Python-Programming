# Write a program which accept one number and display below pattern.
# Input : 5         
# Output :  1
#           1   2
#           1   2   3
#           1   2   3   4
#           1   2   3   4   5
# ----------------------------------------------------------------------------------------------------------------------

def DisplayPattern(Value):
    for i in range(1, Value + 1):
        for j in range(1, i + 1 ):
            print(j, end="  ")
        print()

def main():
    No = int(input("Enter Number : "))

    DisplayPattern(No)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Number : 5
# 1  
# 1  2  
# 1  2  3  
# 1  2  3  4  
# 1  2  3  4  5  

# Enter Number : 3
# 1  
# 1  2  
# 1  2  3  