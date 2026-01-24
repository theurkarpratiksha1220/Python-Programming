# Design a python application that creates two threads.
# - Thread 1 should compute the sum of elements from a list.
# - Thread 2 should compute the product of elements from the same list.
# - Return the result to the main thread and display them.
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

def sum_list(data, result):
    total = 0
    for i in data:
        total = total + i
    result.append(total)

def product_list(data, result):
    prod = 1
    for i in data:
        prod = prod * i
    result.append(prod)

def main():
    start_time = time.time()

    No = int(input("Enter the number of elements: "))
    Data = []

    print("Enter the elements:")
    for _ in range(No):
        Data.append(int(input()))

    print("Actual data is:", Data)

    result = []

    t1 = threading.Thread(target=sum_list, args=(Data, result), name="SumThread")
    t2 = threading.Thread(target=product_list, args=(Data, result), name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", result[0])
    print("Product of elements:", result[1])

    end_time = time.time()
    print("Time required:", end_time - start_time)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the number of elements: 10
# Enter the elements:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Actual data is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sum of elements: 55
# Product of elements: 3628800
# Time required: 7.985609292984009