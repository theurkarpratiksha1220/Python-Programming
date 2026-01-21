# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
#------------------------------------------------------------------------

from functools import reduce

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

RData = reduce(lambda a, b: a + b,Data)
print("Addition of numbers is : ",RData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Addition of numbers is :  55