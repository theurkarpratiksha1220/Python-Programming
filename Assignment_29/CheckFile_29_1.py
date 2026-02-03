# Check File exists in current directory
# Problem statement: write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input: Demo.txt
# Expected Output: Display whether Demo.txt exists or not
# ------------------------------------------------------------------------------------------------------------------------------------------------

import os

def main():
    FileName = input("Enter the name of the file, you want to check in directory : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print(f"{FileName} exists in the current directory.")
    else:
        print(f"{FileName} does not exist in the current directory.")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file, you want to check in directory : Demo.txt
# Demo.txt exists in the current directory.

# Enter the name of the file, you want to check in directory : PQR.txt
# PQR.txt does not exist in the current directory.