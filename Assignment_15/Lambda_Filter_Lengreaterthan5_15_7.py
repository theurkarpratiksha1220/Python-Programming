# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greather than 5.
#------------------------------------------------------------------------

Data = ['Cat', 'Apple', 'Swing', 'PhotoFrame', 'Bus', 'Coconut', 'Peacock']
print("Actual Data is :", Data)

FData = list(filter(lambda a: len(a) > 5, Data))
print("List of strings having length greather than 5 : ",FData)

#------------------------------------------------------------------------
# Output -
# Actual Data is : ['Cat', 'Apple', 'Swing', 'PhotoFrame', 'Bus', 'Coconut', 'Peacock']
# List of strings having length greather than 5 :  ['PhotoFrame', 'Coconut', 'Peacock']