# Write a lambda function which accepts one number and returns True if number is odd otherwise False.
#------------------------------------------------------------------------

No = int(input("Enter Any Number : "))

OddNo = lambda No : No % 2 != 0

Ret = OddNo(No)

print(Ret)

#------------------------------------------------------------------------
# Output -
#Enter Any Number : 11
#True

#Enter Any Number : 2
#False