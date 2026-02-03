# Display File Contents
# Problem statement: write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input: Demo.txt
# Expected Output: Display contents of Demo.txt on console.
# ------------------------------------------------------------------------------------------------------------------------------------------------

import os

def main():
    try:
        FileName = input("Enter the name of the file: ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        print(f"Data from the file - {FileName} is : ")
        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()
       
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file: Demo.txt
# Data from the file - Demo.txt is : 
# Jay Ganesh
# Siyavar Ramchandra ki jay, shree Hanuman ki jay
# End of application

# Enter the name of the file: PQR.txt
# Unable to open file as there is no such file
# End of application