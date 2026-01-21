# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.
#------------------------------------------------------------------------

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Actual Data is :", Data)

FData = list(filter(lambda a: a % 2 == 0 , Data))

CountEvenNumber = len(FData)

print("Count of Even numbers is : ",CountEvenNumber)

#------------------------------------------------------------------------
# Output -
# Actual Data is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Count of Even numbers is :  5