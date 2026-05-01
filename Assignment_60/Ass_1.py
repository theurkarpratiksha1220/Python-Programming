import math

# Inputs
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# 1. Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias
print("Weighted Sum:", weighted_sum)

# 2. Apply sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

output = sigmoid(weighted_sum)

# 3. Display final output
print("Final Output (after sigmoid):", output)

# 4. Explanation
if output > 0.5:
    print("The output is closer to 1.")
else:
    print("The output is closer to 0.")