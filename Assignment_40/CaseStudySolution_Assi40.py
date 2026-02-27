print("================================================================")
print("Student Performance Prediction using Decision Tree Classifier")
print("================================================================")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ================================================================
# 1. Load Dataset
# ================================================================

data = pd.read_csv("student_performance_ml.csv")

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset Shape:", data.shape)
print("\nMissing Values:\n", data.isnull().sum())
print("\nClass Distribution:\n", data['FinalResult'].value_counts())

# ================================================================
# 2. Train-Test Split (Full Features)
# ================================================================

X = data[['StudyHours', 'Attendance', 'PreviousScore',
          'AssignmentsCompleted', 'SleepHours']]

Y = data['FinalResult']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# ================================================================
# 3. Train Decision Tree
# ================================================================

dt_model = DecisionTreeClassifier(max_depth=None, random_state=42)
dt_model.fit(X_train, Y_train)

y_pred = dt_model.predict(X_test)

train_accuracy = accuracy_score(Y_train, dt_model.predict(X_train))
test_accuracy = accuracy_score(Y_test, y_pred)

print("\nTraining Accuracy:", train_accuracy)
print("Testing Accuracy :", test_accuracy)

# ================================================================
# 4. Feature Importance
# ================================================================

print("\nFeature Importances:")
importances = dt_model.feature_importances_

for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.4f}")

print("Most Important Feature:", X.columns[np.argmax(importances)])
print("Least Important Feature:", X.columns[np.argmin(importances)])

# ================================================================
# 5. Remove SleepHours & Retrain
# ================================================================

X_no_sleep = data[['StudyHours', 'Attendance',
                   'PreviousScore', 'AssignmentsCompleted']]

X_train_ns, X_test_ns, Y_train_ns, Y_test_ns = train_test_split(
    X_no_sleep, Y, test_size=0.3, random_state=42
)

model_ns = DecisionTreeClassifier(random_state=42)
model_ns.fit(X_train_ns, Y_train_ns)

accuracy_no_sleep = accuracy_score(
    Y_test_ns, model_ns.predict(X_test_ns)
)

print("\nAccuracy without SleepHours:", accuracy_no_sleep)

# ================================================================
# 6. Only StudyHours & Attendance
# ================================================================

X_small = data[['StudyHours', 'Attendance']]

X_train_s, X_test_s, Y_train_s, Y_test_s = train_test_split(
    X_small, Y, test_size=0.3, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(X_train_s, Y_train_s)

accuracy_small = accuracy_score(
    Y_test_s, model_small.predict(X_test_s)
)

print("Accuracy with only StudyHours & Attendance:", accuracy_small)

# ================================================================
# 7. Predict 5 New Students
# ================================================================

new_students = pd.DataFrame({
    'StudyHours': [5, 2, 7, 4, 6],
    'Attendance': [80, 50, 90, 65, 75],
    'PreviousScore': [70, 40, 85, 60, 72],
    'AssignmentsCompleted': [8, 3, 9, 6, 7],
    'SleepHours': [7, 6, 8, 5, 7]
})

predictions = dt_model.predict(new_students)
new_students['Predicted_Result'] = predictions
new_students['Predicted_Result'] = new_students['Predicted_Result'].map(
    {1: "Pass", 0: "Fail"}
)

print("\nPredictions for 5 New Students:")
print(new_students)

# ================================================================
# 8. Manual Accuracy Calculation
# ================================================================

correct = (Y_test == y_pred).sum()
total = len(Y_test)
manual_accuracy = correct / total

print("\nManual Accuracy:", manual_accuracy)
print("Sklearn Accuracy:", test_accuracy)

# ================================================================
# 9. Misclassified Students
# ================================================================

misclassified_mask = (Y_test != y_pred)

misclassified = X_test[misclassified_mask].copy()
misclassified['Actual'] = Y_test[misclassified_mask]
misclassified['Predicted'] = y_pred[misclassified_mask]

print("\nMisclassified Students:")
print(misclassified)
print("Total Misclassified:", len(misclassified))

# ================================================================
# 10. Different random_state Comparison
# ================================================================

print("\nAccuracy with different random_state values:")

for rs in [0, 10, 42]:
    X_train_rs, X_test_rs, Y_train_rs, Y_test_rs = train_test_split(
        X, Y, test_size=0.3, random_state=rs
    )

    model_rs = DecisionTreeClassifier(random_state=rs)
    model_rs.fit(X_train_rs, Y_train_rs)

    acc = accuracy_score(Y_test_rs,
                         model_rs.predict(X_test_rs))

    print(f"Random State {rs} → Accuracy: {acc:.4f}")

# ================================================================
# 11. Decision Tree Visualization
# ================================================================

plt.figure(figsize=(20,10))
plot_tree(dt_model,
          feature_names=X.columns,
          class_names=["Fail", "Pass"],
          filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# ================================================================
# 12. Add PerformanceIndex Feature
# ================================================================

data['PerformanceIndex'] = (data['StudyHours'] * 2) + data['Attendance']

X_new = data[['StudyHours', 'Attendance', 'PreviousScore',
              'AssignmentsCompleted', 'SleepHours',
              'PerformanceIndex']]

X_train_pi, X_test_pi, Y_train_pi, Y_test_pi = train_test_split(
    X_new, Y, test_size=0.3, random_state=42
)

model_pi = DecisionTreeClassifier(random_state=42)
model_pi.fit(X_train_pi, Y_train_pi)

accuracy_pi = accuracy_score(
    Y_test_pi, model_pi.predict(X_test_pi)
)

print("\nAccuracy with PerformanceIndex:", accuracy_pi)

# ================================================================
# 13. Overfitting Check
# ================================================================

print("\nOverfitting Check:")
print("Training Accuracy:", train_accuracy)
print("Testing Accuracy :", test_accuracy)

if train_accuracy == 1.0 and test_accuracy < train_accuracy:
    print("Model is overfitting (memorizing training data).")
elif train_accuracy - test_accuracy > 0.1:
    print("Model may be overfitting.")
else:
    print("Model is balanced.")
