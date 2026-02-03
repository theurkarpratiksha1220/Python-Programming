# Display File line by line
# Problem statement: write a program which accepts a file name form the user and displays the contents of the file line by line on the screen
# Input(Command line): Demo.txt
# Expected Output: Display each line of Demo.txt one by one
# -----------------------------------------------------------------------------------------------------------------------------

def main():
    FileName = input("Enter the name of the file: ")

    try:
        File = open(FileName, 'r')
        
        for line in File:
            print(line, end='')
        print()

    except FileNotFoundError:
        print(f"The file '{FileName}' does not exist.")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the name of the file: Demo.txt
# Jay Ganesh
# Siyavar Ramchandra ki jay, shree Hanuman ki jay