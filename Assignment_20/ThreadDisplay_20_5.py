# Design a python application that creates two threads named Thread1 and Thread2.
# - Thread1 should display numbers from 1 to 50.
# - Thread2 should display numbers from 50 to 1 in reverse order.
# - Ensure that:
#     - Thread2 starts execution only after Thread1 has completed.
# - Use appropriate thread synchronization.
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

def DisplayNo():
    for i in range(1, 51):
        print("Thread1: ", i)

def DisplayReverse():
    for i in range(50, 0, -1):
        print("Thread2: ", i)

def main():

    t1 = threading.Thread(target=DisplayNo, name="Thread1")
    t2 = threading.Thread(target=DisplayReverse, name="Thread2")

    start_time = time.time()

    t1.start()
    t1.join()

    end_time = time.time()

    print("time required :",end_time-start_time)

    start_time = time.time()

    t2.start()
    t2.join()

    end_time = time.time()

    print("time required :",end_time-start_time)

    print("Completed Execution.")

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Thread1:  1
# Thread1:  2
# Thread1:  3
# Thread1:  4
# Thread1:  5
# Thread1:  6
# Thread1:  7
# Thread1:  8
# Thread1:  9
# Thread1:  10
# Thread1:  11
# Thread1:  12
# Thread1:  13
# Thread1:  14
# Thread1:  15
# Thread1:  16
# Thread1:  17
# Thread1:  18
# Thread1:  19
# Thread1:  20
# Thread1:  21
# Thread1:  22
# Thread1:  23
# Thread1:  24
# Thread1:  25
# Thread1:  26
# Thread1:  27
# Thread1:  28
# Thread1:  29
# Thread1:  30
# Thread1:  31
# Thread1:  32
# Thread1:  33
# Thread1:  34
# Thread1:  35
# Thread1:  36
# Thread1:  37
# Thread1:  38
# Thread1:  39
# Thread1:  40
# Thread1:  41
# Thread1:  42
# Thread1:  43
# Thread1:  44
# Thread1:  45
# Thread1:  46
# Thread1:  47
# Thread1:  48
# Thread1:  49
# Thread1:  50
# time required : 0.00023984909057617188
# Thread2:  50
# Thread2:  49
# Thread2:  48
# Thread2:  47
# Thread2:  46
# Thread2:  45
# Thread2:  44
# Thread2:  43
# Thread2:  42
# Thread2:  41
# Thread2:  40
# Thread2:  39
# Thread2:  38
# Thread2:  37
# Thread2:  36
# Thread2:  35
# Thread2:  34
# Thread2:  33
# Thread2:  32
# Thread2:  31
# Thread2:  30
# Thread2:  29
# Thread2:  28
# Thread2:  27
# Thread2:  26
# Thread2:  25
# Thread2:  24
# Thread2:  23
# Thread2:  22
# Thread2:  21
# Thread2:  20
# Thread2:  19
# Thread2:  18
# Thread2:  17
# Thread2:  16
# Thread2:  15
# Thread2:  14
# Thread2:  13
# Thread2:  12
# hread2:  11
# Thread2:  10
# Thread2:  9
# Thread2:  8
# Thread2:  7
# Thread2:  6
# Thread2:  5
# Thread2:  4
# Thread2:  3
# Thread2:  2
# hread2:  1
# time required : 0.0002129077911376953
# Completed Execution.