# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
#------------------------------------------------------------------------

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

MData = list(map(lambda No : No * No,Data))
print("Square of each number : ",MData)

#------------------------------------------------------------------------
# Output -
#Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Square of each number :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]