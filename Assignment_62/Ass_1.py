# Input Image (5x5)
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Kernel (3x3 edge detection)
kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Output feature map size = (5-3+1) x (5-3+1) = 3x3
feature_map = [[0 for _ in range(3)] for _ in range(3)]

# 1. Move kernel over image
for i in range(3):
    for j in range(3):
        print(f"\nRegion at position ({i},{j}):")
        
        result = 0
        calculation = ""

        # 2. Perform multiplication and addition
        for ki in range(3):
            for kj in range(3):
                val = image[i + ki][j + kj]
                k = kernel[ki][kj]
                
                print(f"{val} ", end="")
                result += val * k
                calculation += f"{val}*{k} + "
            print()

        # Remove last '+'
        calculation = calculation[:-3]

        # Print calculation
        print("Calculation:")
        print(calculation)
        print("Output =", result)

        # 3. Store in feature map
        feature_map[i][j] = result

# 4. Print final feature map
print("\nFinal Feature Map:")
for row in feature_map:
    print(row)