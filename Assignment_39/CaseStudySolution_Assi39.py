print("================================================================")
print("Student Performance Prediction using Decision Tree Classifier")
print("================================================================")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

print("================================================================")
print("1. Dataset Loading")
print("================================================================")

data = pd.read_csv("student_performance_ml.csv")
print("Dataset Loaded Successfully.\n")
print("First 5 rows of the dataset:")
print(data.head())

print("================================================================")
print("2. Data Analysis")
print("================================================================")

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nDataset Info:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

print("\nCheck for missing values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())

print("\nClass Distribution:")
print(data['FinalResult'].value_counts())

print("\nCorrelation with FinalResult:")
print(data.corr()['FinalResult'].sort_values(ascending=False))

print("================================================================")
print("3. Data Visualization")
print("================================================================")

# Pairplot to visualize relationships between features
sns.pairplot(data, hue="FinalResult")
plt.suptitle("Pairplot of Student Features vs Final Result", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Features")
plt.show()

print("================================================================")
print("4. Train-Test Split")
print("================================================================")

X = data[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
Y = data['FinalResult']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
print("\nData split into training and testing sets successfully.")

print("================================================================")
print("5. Train Three Decision Tree Models with Different Depths")
print("================================================================")

depth_values = [1, 3, None]
test_accuracies = {}

print("\nComparing Decision Tree Models with Different max_depth:\n")

for depth in depth_values:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)

    test_accuracies[depth] = accuracy
    print(f"max_depth = {depth}, Testing Accuracy = {accuracy*100:.2f}%")

print("================================================================")
print("6. Choose Best Model (max_depth=None used as default model)")
print("================================================================")

dt_model = DecisionTreeClassifier(max_depth=None, random_state=42)
dt_model.fit(X_train, Y_train)

y_pred = dt_model.predict(X_test)

#Obervation 
#The model with max_depth=1 shows lower accuracy due to underfitting.
#The model with max_depth=3 provides balanced performance.
#The model with max_depth=None achieves highest training accuracy but may overfit.

print("================================================================")
print("7. Training and Testing Accuracy")
print("================================================================")

train_accuracy = accuracy_score(Y_train, dt_model.predict(X_train))
test_accuracy = accuracy_score(Y_test, y_pred)

print(f"\nTraining Accuracy (max_depth=None): {train_accuracy*100:.2f}%")
print(f"Testing Accuracy  (max_depth=None): {test_accuracy*100:.2f}%")

# Overfitting / Underfitting Check
if train_accuracy - test_accuracy > 0.1:
    print("Observation: Model may be overfitting.")
elif test_accuracy - train_accuracy > 0.1:
    print("Observation: Model may be underfitting.")
else:
    print("Observation: Model is well balanced.")

print("================================================================")
print("8. Confusion Matrix")
print("================================================================")

cm = confusion_matrix(Y_test, Y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

print("\nConfusion Matrix Explanation:")
print("True Positive  (TP): Predicted Pass & Actually Pass")
print("True Negative  (TN): Predicted Fail & Actually Fail")
print("False Positive (FP): Predicted Pass but Actually Fail")
print("False Negative (FN): Predicted Fail but Actually Pass")

print("================================================================")
print("9. Predict New Student")
print("================================================================")

new_student = pd.DataFrame({
    'StudyHours': [6],
    'Attendance': [85],
    'PreviousScore': [66],
    'AssignmentsCompleted': [7],
    'SleepHours': [7]
})

prediction = dt_model.predict(new_student)
result = "Pass" if prediction[0] == 1 else "Fail"

print(f"\nPrediction for the new student: {result}")

print("================================================================")
print("10. Observations and Conclusion")
print("================================================================")

print("\nModel Comparison Observations:")

for depth, acc in test_accuracies.items():
    print(f"Depth {depth}: {acc*100:.2f}% accuracy")

print("\nFinal Conclusion:")
print("• max_depth=1 → Very simple model (may underfit).")
print("• max_depth=3 → Balanced model with moderate complexity.")
print("• max_depth=None → Fully grown tree (may overfit).")
print("The best depth is the one giving highest testing accuracy.")
print(f"The student with given details is predicted to: {result}")