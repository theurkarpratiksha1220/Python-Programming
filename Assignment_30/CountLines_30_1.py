# Count lines in a file
# Problem statement: write a program which accepts a file name from the user and counts how many lines are present in the file
# Input: Demo.txt
# Expected Output: Total number of lines in Demo.txt
# -----------------------------------------------------------------------------------------------------------------------------

def main():
    FileName = input("Enter the name of the file: ")

    try:
        File = open(FileName, 'r')
        lines = File.readlines()
        
        line_count = len(lines)

        print(f"Total number of lines in '{FileName}': {line_count}")

    except FileNotFoundError:
        print(f"The file '{FileName}' does not exist.")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file: PQR.txt
# The file 'PQR.txt' does not exist.

# Enter the name of the file: Demo.txt
# Total number of lines in 'Demo.txt': 2