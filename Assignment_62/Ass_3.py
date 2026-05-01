# 1. Input 2D matrix
matrix = [
    [6, 4],
    [8, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 2. Flatten the matrix (2D → 1D)
flatten_output = []
for row in matrix:
    for val in row:
        flatten_output.append(val)

print("\nFlatten Output:", flatten_output)

# 3. Fully Connected Layer (example weights + bias)
weights = [0.2, 0.4, 0.6, 0.8]
bias = 1

# 4. Manual calculation (dot product + bias)
result = 0
calculation = ""

for i in range(len(flatten_output)):
    result += flatten_output[i] * weights[i]
    calculation += f"{flatten_output[i]}*{weights[i]} + "

calculation = calculation[:-3]  # remove last '+'

result += bias

print("\nCalculation:")
print(calculation + f" + {bias}")

print("\nFinal Output:", result)