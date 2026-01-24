# Write a program which accept name from user and display length of its name.
# Input : Marvellous          Output :  10
# ----------------------------------------------------------------------------------------------------------------------

def DisplayLength(Value1):
    print(len(Value1))

def main():

    Value = input("Enter Name : ")

    DisplayLength(Value)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter Name : Marvellous
# 10

# Enter Name : pratiksha
# 9