# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.
#------------------------------------------------------------------------

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

FData = list(filter(lambda No : No % 2 == 0,Data))
print("List of Even numbers is : ",FData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List of Even numbers is :  [2, 4, 6, 8, 10]