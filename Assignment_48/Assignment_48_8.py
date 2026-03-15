from sklearn.metrics import confusion_matrix

Border = '-'*40

#------------ Actual and predicted values ------------#
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

#------------ Compute confusion matrix ------------#
cm = confusion_matrix(actual, predicted)

print(Border)
print("Confusion Matrix is : \n")
print(cm)
print(Border)

#------------ Extract TN, FP, FN, TP ------------#
TN, FP, FN, TP = cm.ravel()

#------------ Display results ------------#
print("Values are as follows: \n")
print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)
print(Border)

