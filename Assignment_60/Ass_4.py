# Simple ANN weight update (single neuron)

# 1. Inputs
x = 2                  # input
w = 0.5                # initial weight
bias = 0.1             # bias
target = 1             # target output
learning_rate = 0.01   # learning rate

# Activation function (linear for simplicity)
def predict(x, w, b):
    return x * w + b

# 2. Calculate prediction
y_pred = predict(x, w, bias)

# 3. Calculate error
error = target - y_pred

# 4. Gradient descent weight update
# derivative of loss (MSE) w.r.t weight = -2 * x * error
gradient = -2 * x * error
new_w = w - learning_rate * gradient

# Update bias similarly
bias_gradient = -2 * error
new_bias = bias - learning_rate * bias_gradient

# 5. Display results
print("Old Weight:", w)
print("Updated Weight:", new_w)

print("Old Bias:", bias)
print("Updated Bias:", new_bias)

print("Prediction:", y_pred)
print("Error:", error)