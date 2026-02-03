# Copy File Contents into a New File (Command Line)
# Problem statement: write a program which accepts an existing file name through 
# command line arguments, creates a new file named Demo.txt, and copies all Contents
#  from the given file into Demo.txt
# Input(Command line): ABC.txt
# Expected Output: Create Demo.txt and copy contents of ABC.txt into Demo.txt.
# ------------------------------------------------------------------------------------------------------------------------------------------------

import sys

def main():

    if len(sys.argv) != 2:
        print("Enter valid file name in proper sequence")
        return

    ExistFile = sys.argv[1]
    TargetFile = "Demo.txt"

    try:
        file1 = open(ExistFile, "r")
        content = file1.read()

        file2 = open(TargetFile, "w")
        file2.write(content)

        print(f"Contents of '{ExistFile}' copied successfully into '{TargetFile}'")

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# > python CopyFileContent_29_3.py 
# Enter valid file name in proper sequence

# > python CopyFileContent_29_3.py ABC.txt
# Contents of 'ABC.txt' copied successfully into 'Demo.txt'