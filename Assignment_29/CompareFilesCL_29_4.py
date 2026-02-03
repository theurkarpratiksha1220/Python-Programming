# Compare Two Files(Command Line)
# Problem statement: write a program which accepts two file names through command line arguments and compares the contents of both files.
# - If both files contain the same contents, display Success
# - Otherwise display Failure
# Input(Command line): Demo.txt Hello.txt
# Expected Output: Success or failure
# ------------------------------------------------------------------------------------------------------------------------------------------------

import sys

def main():
    if len(sys.argv) != 3:
        print("Please provide two files - python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        fobj1 = open(file1, 'r')
        fobj2 = open(file2, 'r')

        if fobj1.read() == fobj2.read():
            print("Success")
        else:
            print("Failure")

    except FileNotFoundError:
        print("One or both files not found")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# In Command prompt > python CompareFilesCl_29_4.py
# Please provide two files - python compare_files.py <file1> <file2>

# In Command prompt > python CompareFilesCl_29_4.py Demo.txt
# Please provide two files - python compare_files.py <file1> <file2>

# In Command prompt > python CompareFilesCl_29_4.py Demo.txt Hello.txt     #(if Demo.txt file exists and Hello.txt file is not)
# One or both files not found

# In Command prompt > python CompareFilesCl_29_4.py Demo.txt Hello.txt     #(if both file exists and content same)
# Success

# In Command prompt > python CompareFilesCl_29_4.py Demo.txt Hello.txt     #(if both files exists but content are not same)
# Failure
