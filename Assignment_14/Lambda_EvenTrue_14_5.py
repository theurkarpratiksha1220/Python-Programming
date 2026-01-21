# Write a lambda function which accepts one number and returns True if number is even otherwise False.
#------------------------------------------------------------------------

No = int(input("Enter Any Number : "))

EvenNo = lambda No : No % 2 == 0

Ret = EvenNo(No)

print(Ret)

#------------------------------------------------------------------------
# Output -
# Enter Any Number : 2
# True

# Enter Any Number : 11
# False