# Write a program which accepts one number and prints binary equivalent.
#-------------------------------------------------------------------------------------------------------

import math

def BinaryEqui(Value):                                                      
    return bin(Value)[2:]

def main():

        No = int(input("Enter a number : ")) 

        Binary = BinaryEqui(No)
        print(Binary)

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------
# Output
#Enter a number : 10
#1010

#Enter a number : 20
#10100