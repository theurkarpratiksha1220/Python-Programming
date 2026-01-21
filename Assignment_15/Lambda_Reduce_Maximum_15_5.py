# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
#------------------------------------------------------------------------

from functools import reduce

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

RData = reduce(lambda No1, No2 : No1 if No1 > No2 else No2,Data)
print("Maximum number is : ",RData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Mximum number is :  10