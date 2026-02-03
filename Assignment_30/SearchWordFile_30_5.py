# Search a Word in File
# Problem statement: write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input: Demo.txt Marvellous
# Expected Output: Display whether the word Marvellous is found in Demo.txt or not.
# -------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    FileName = input("Enter the file name: ")
    SearchWord = input("Enter the word to search: ")

    try:
        File = open(FileName, 'r')
        content = File.read()

        if SearchWord in content:
            print(f"The word '{SearchWord}' is found in '{FileName}'.")
        else:
            print(f"The word '{SearchWord}' is not found in '{FileName}'.")

    except FileNotFoundError:
        print(f"The file '{FileName}' does not exist.")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the file name: Demo.txt
# Enter the word to search: Jay
# The word 'Jay' is found in 'Demo.txt'.

# Enter the file name: Demo.txt
# Enter the word to search: Marvellous
# The word 'Marvellous' is not found in 'Demo.txt'.