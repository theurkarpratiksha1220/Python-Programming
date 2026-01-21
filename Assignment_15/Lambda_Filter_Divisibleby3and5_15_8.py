# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5
#------------------------------------------------------------------------

Data = [1, 2, 3, 6, 9, 11, 5, 15, 25, 26, 13, 30]
print("Actual Data is :", Data)

FData = list(filter(lambda a: (a % 3 == 0 and a % 5 == 0), Data))
print("List of numbers divisible by both 3 and 5: ",FData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 6, 9, 11, 5, 15, 25, 26, 13, 30]
# List of numbers divisible by both 3 and 5:  [15, 30]