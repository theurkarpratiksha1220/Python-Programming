# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -------------------------------
# Part 1: Data Preprocessing
# -------------------------------

# Load datasets
fake_df = pd.read_csv("fake.csv")
true_df = pd.read_csv("true.csv")

# Add labels
fake_df["label"] = 0   # Fake
true_df["label"] = 1   # Real

# Combine datasets
df = pd.concat([fake_df, true_df], axis=0)

# Drop null values
df = df.dropna()

# Use 'text' column (you can also use title or combine both)
X = df["text"]
Y = df["label"]

# -------------------------------
# Part 2: Feature Extraction
# -------------------------------

# Convert text to TF-IDF features
tfidf = TfidfVectorizer(stop_words="english", max_df=0.7)

X_tfidf = tfidf.fit_transform(X)

# Train-test split
X_train, X_test,Y_train, Y_test = train_test_split(
    X_tfidf, Y, test_size=0.2, random_state=42
)

# -------------------------------
# Part 3: Model Training
# -------------------------------

# Individual models
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier()

# Train models
lr.fit(X_train, Y_train)
dt.fit(X_train, Y_train)

# Voting Classifier - Hard Voting
hard_vote = VotingClassifier(
    estimators=[("lr", lr), ("dt", dt)],
    voting="hard"
)
hard_vote.fit(X_train, Y_train)

# Voting Classifier - Soft Voting
soft_vote = VotingClassifier(
    estimators=[("lr", lr), ("dt", dt)],
    voting="soft"
)
soft_vote.fit(X_train, Y_train)

# -------------------------------
# Part 4: Evaluation
# -------------------------------

# Predictions
lr_pred = lr.predict(X_test)
dt_pred = dt.predict(X_test)
hard_pred = hard_vote.predict(X_test)
soft_pred = soft_vote.predict(X_test)

# Accuracy
print("Logistic Regression Accuracy:", accuracy_score(Y_test, lr_pred))
print("Decision Tree Accuracy:", accuracy_score(Y_test, dt_pred))
print("Hard Voting Accuracy:", accuracy_score(Y_test, hard_pred))
print("Soft Voting Accuracy:", accuracy_score(Y_test, soft_pred))

# Confusion Matrices
print("\nConfusion Matrix - Logistic Regression")
print(confusion_matrix(Y_test, lr_pred))

print("\nConfusion Matrix - Decision Tree")
print(confusion_matrix(Y_test, dt_pred))

print("\nConfusion Matrix - Hard Voting")
print(confusion_matrix(Y_test, hard_pred))

print("\nConfusion Matrix - Soft Voting")
print(confusion_matrix(Y_test, soft_pred))

# Classification Report 
print("\nClassification Report (Soft Voting)")
print(classification_report(Y_test, soft_pred))