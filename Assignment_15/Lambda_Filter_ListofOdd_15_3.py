# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.
#------------------------------------------------------------------------

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

FData = list(filter(lambda No : No % 2 != 0,Data))
print("List of Odd numbers is : ",FData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List of Odd numbers is :  [1, 3, 5, 7, 9]
