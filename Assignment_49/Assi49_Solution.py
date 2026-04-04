# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("diabetes.csv")

# -------------------------------
# 1. EDA
# -------------------------------
print("First 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

# Target distribution
sns.countplot(x='Outcome', data=df)
plt.title("Outcome Distribution")
plt.show()

# Histogram
df.hist(figsize=(10,8))
plt.show()

# Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 2. Data Preprocessing
# -------------------------------

# Replace 0 with NaN (important medical fields)
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols] = df[cols].replace(0, np.nan)

# Fill missing values with median
df.fillna(df.median(), inplace=True)

# Split features and target
X = df.drop('Outcome', axis=1)
Y = df['Outcome']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y, test_size=0.2, random_state=42
)

# -------------------------------
# 3. Model Building
# -------------------------------

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, Y_train)
Y_pred_lr = lr.predict(X_test)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
Y_pred_knn = knn.predict(X_test)

# -------------------------------
# 4. Evaluation
# -------------------------------

def evaluate(name, Y_test, Y_pred):
    print(f"\n{name} Results")
    print("Accuracy:", accuracy_score(Y_test, Y_pred))
    print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
    print("Report:\n", classification_report(Y_test, Y_pred))

    sns.heatmap(confusion_matrix(Y_test, Y_pred),
                annot=True, fmt='d', cmap='Blues')
    plt.title(name)
    plt.show()

evaluate("Logistic Regression", Y_test, Y_pred_lr)
evaluate("KNN", Y_test, Y_pred_knn)

# -------------------------------
# 5. Final Prediction
# -------------------------------

# Predict first 10 test values
pred = lr.predict(X_test[:10])

print("\nSample Predictions:")
print(pred)

# Save to CSV
output = pd.DataFrame({
    "Actual": Y_test[:10].values,
    "Predicted": pred
})

output.to_csv("predictions.csv", index=False)
print("Saved to predictions.csv")