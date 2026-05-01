import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Create dataset
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9], 
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# 3. Apply StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Train FNN model
model = MLPClassifier(hidden_layer_sizes=(5, 5), max_iter=1000, random_state=42)
model.fit(X_train, Y_train)

# 5. Evaluate accuracy
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print("Model Accuracy:", accuracy)

# Test input
new_customer = np.array([[46, 1450, 5, 6, 91]])

# Apply same scaling
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

# Output result
if prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")