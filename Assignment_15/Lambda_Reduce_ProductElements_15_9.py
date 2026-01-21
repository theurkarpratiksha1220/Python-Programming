# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements
#------------------------------------------------------------------------

from functools import reduce

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

RData = reduce(lambda a, b: a * b, Data)
print("List of product of elements: ",RData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List of product of elements:  3628800