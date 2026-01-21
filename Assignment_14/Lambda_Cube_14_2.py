# Write a lambda function which accepts one number and returns cube of that number.
#------------------------------------------------------------------------

No = int(input("Enter Any Number : "))

Cube = lambda No : No * No * No

Ret = Cube(No)

print("Cube of a number is : ",Ret)

#------------------------------------------------------------------------
# Output -
# Enter Any Number : 3
# Cube of a number is :  27