# Copy File Contents into Another File
# Problem statement: write a program which accepts two file names from the user First file is an existing file
# Second file is a new file. Copy all Contents from the first file into the second file.
# Input: Abc.txt Demo.txt
# Expected Output: Contents of ABC.txt copied into Demo.txt
# -----------------------------------------------------------------------------------------------------------------------------

def main():

    ExistFile = input("Enter the name of the existing file: ")
    NewTargetFile = input("Enter the name of new target file: ")

    try:
        file1 = open(ExistFile, "r")
        content = file1.read()

        file2 = open(NewTargetFile, "w")
        file2.write(content)

        print(f"Contents of '{ExistFile}' copied successfully into '{NewTargetFile}'.")

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the existing file: Demo.txt
# Enter the name of new target file: ABC.txt
# Contents of 'Demo.txt' copied successfully into 'ABC.txt'.
