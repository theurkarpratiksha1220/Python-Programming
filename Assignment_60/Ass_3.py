import math

# 3. Actual and predicted values
actual = [1, 0, 1, 1]
predicted = [0.9, 0.2, 0.8, 0.7]

# 1. Mean Squared Error (MSE)
def mean_squared_error(y_true, y_pred):
    n = len(y_true)
    mse = sum((y_true[i] - y_pred[i])**2 for i in range(n)) / n
    return mse

# 2. Binary Cross Entropy (BCE)
def binary_cross_entropy(y_true, y_pred):
    n = len(y_true)
    epsilon = 1e-10  # to avoid log(0)
    bce = 0
    for i in range(n):
        y = y_true[i]
        p = min(max(y_pred[i], epsilon), 1 - epsilon)
        bce += y * math.log(p) + (1 - y) * math.log(1 - p)
    return -bce / n

# 4. Display losses
mse_loss = mean_squared_error(actual, predicted)
bce_loss = binary_cross_entropy(actual, predicted)

print("Mean Squared Error:", mse_loss)
print("Binary Cross Entropy:", bce_loss)


# MSE → Regression
# Binary Cross Entropy → Classification (binary)