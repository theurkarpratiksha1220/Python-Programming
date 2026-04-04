# ===============================
# Bank Term Deposit Prediction
# ===============================

#--------------------------------
# 1. Import Libraries
#--------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#--------------------------------
# 2. Load Dataset
#--------------------------------

df = pd.read_csv("bank-full.csv", sep=';')

#--------------------------------
# 3. Explore Data
#--------------------------------

print(df.head())
print(df.info())
print(df.describe())

# Replace 'unknown' with NaN and drop
df.replace("unknown", np.nan, inplace=True)
df.dropna(inplace=True)

# Target distribution
sns.countplot(x='y', data=df)
plt.title("Target Distribution")
plt.show()

#--------------------------------
# 4. Preprocessing
#--------------------------------

# Convert target to binary
df['y'] = df['y'].map({'yes': 1, 'no': 0})

# Label Encoding categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Feature and Target split
X = df.drop('y', axis=1)
y = df['y']

#---------------------------------------------------
# 5. Train-Test Split (before scaling)
#---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#--------------------------------
# 6. Feature Scaling (AFTER split)
#--------------------------------

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#--------------------------------
# 7. Train Models
#--------------------------------

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

#--------------------------------
# 8. Evaluation Function
#--------------------------------

def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print(f"\n{name} Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("ROC-AUC:", roc_auc_score(y_test, y_prob))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=name)

#--------------------------------
# 9. Evaluate Models
#--------------------------------

plt.figure(figsize=(8,6))

evaluate_model(lr, X_test, y_test, "Logistic Regression")
evaluate_model(knn, X_test, y_test, "KNN")
evaluate_model(rf, X_test, y_test, "Random Forest")

# Final ROC Curve
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()