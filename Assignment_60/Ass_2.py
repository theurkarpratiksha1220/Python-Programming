import numpy as np
import matplotlib.pyplot as plt

# 1. Input values from -10 to 10
x = np.linspace(-10, 10, 100)

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Compute outputs
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# 2. Plotting
plt.figure(figsize=(10, 6))

plt.plot(x, y_sigmoid, label="Sigmoid", color="blue")
plt.plot(x, y_relu, label="ReLU", color="green")
plt.plot(x, y_tanh, label="Tanh", color="red")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.grid()

plt.show()


# 1. Sigmoid Function
# Formula: 1 / (1 + e^-x)
# Output range: 0 to 1
# Use: Commonly used in binary classification, Acts like a probability

# 2. ReLU (Rectified Linear Unit)
# Formula: max(0, x)
# Output range: 0 to ∞
# Use: Most widely used in deep learning models, Efficient and simple

# 3. Tanh (Hyperbolic Tangent)
# Formula: (e^x - e^-x) / (e^x + e^-x)
# Output range: -1 to 1
# Use: Preferred over sigmoid in some cases because it is zero-centered
