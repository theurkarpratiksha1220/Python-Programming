# Write a lambda function which accepts one number and returns True if divisible by 5.
#------------------------------------------------------------------------

No = int(input("Enter Any Number : "))

Divisible5No = lambda No : No % 5 == 0

Ret = Divisible5No(No)

print(Ret)

#------------------------------------------------------------------------
# Output -
#Enter Any Number : 5
#True

#Enter Any Number : 6
#False