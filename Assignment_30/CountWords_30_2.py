# Count Words in a file
# Problem statement: write a program which accepts a file name from the user and counts the total number of words in that file
# Input: Demo.txt
# Expected Output: Total number of words in Demo.txt
# -----------------------------------------------------------------------------------------------------------------------------

def main():
    FileName = input("Enter the name of the file: ")

    try:
        File = open(FileName, 'r')
        ContentFile = File.read()
        
        Words = ContentFile.split()

        WordCount = len(Words)

        print(f"Total number of words in '{FileName}': {WordCount}")

    except FileNotFoundError:
        print(f"The file '{FileName}' does not exist.")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file: Demo.txt
# Total number of words in 'Demo.txt': 10

