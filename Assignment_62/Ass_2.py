# Input Feature Map
feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# 1. Display original feature map
print("Original Feature Map:")
for row in feature_map:
    print(row)

# 2. Apply ReLU
relu_output = []
for row in feature_map:
    relu_row = []
    for val in row:
        if val < 0:
            relu_row.append(0)
        else:
            relu_row.append(val)
    relu_output.append(relu_row)

print("\nAfter ReLU:")
for row in relu_output:
    print(row)

# 3. Apply 2x2 Max Pooling (stride = 2)
pool_size = 2
stride = 2

pooled_output = []

for i in range(0, len(relu_output) - pool_size + 1, stride):
    row = []
    for j in range(0, len(relu_output[0]) - pool_size + 1, stride):
        
        # Extract 2x2 region
        region = [
            relu_output[i][j], relu_output[i][j+1],
            relu_output[i+1][j], relu_output[i+1][j+1]
        ]
        
        print(f"\nPooling Region at ({i},{j}):", region)
        
        # Take max
        max_val = max(region)
        print("Max Value:", max_val)
        
        row.append(max_val)
    
    pooled_output.append(row)

# 4. Display pooled output
print("\nAfter Max Pooling:")
for row in pooled_output:
    print(row)