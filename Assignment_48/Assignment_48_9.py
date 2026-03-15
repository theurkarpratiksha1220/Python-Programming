from sklearn.metrics import classification_report

Border = '-'*40

#------------ Define the actual and predicted values ------------#
actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

#------------ Generate the classification report ------------#
report = classification_report(actual, predicted, target_names=['Class 0', 'Class 1'])

#------------ Display the report ------------#
print(Border)
print("Classification Report is as below:\n")
print(report)
print(Border)