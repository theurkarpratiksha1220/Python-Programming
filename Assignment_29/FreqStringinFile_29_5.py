# Frequency of a string in File
# Problem statement: write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input: Demo.txt Marvellous
# Expected Output: Count how many times “Marvellous” appears in Demo.txt
# ------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    FileName = input("Enter the name of the file: ")
    StringUser = input("Enter a string you want to search in file: ")

    try:
        fobj = open(FileName, 'r')
        content = fobj.read()

        count_string = content.lower().count(StringUser.lower())

        print(f"The string '{StringUser}' appears {count_string} times in the file '{FileName}'.")

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file: Demo1.txt
# Enter a string you want to search in file: Marvellous
# The string 'Marvellous' appears 4 times in the file 'Demo1.txt'.

# Enter the name of the file: Demo1.txt
# Enter a string you want to search in file: marvellous
# The string 'marvellous' appears 4 times in the file 'Demo1.txt'.

# Enter the name of the file: Demo1.txt
# Enter a string you want to search in file: team
# The string 'team' appears 0 times in the file 'Demo1.txt'.
