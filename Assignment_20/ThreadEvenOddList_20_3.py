# Design a python application that creates two threads named EvenList and OddList.
# - Both threads should accept a list of integers as input.
# - The EvenList thread should:
#              - Extract all even elements from the list.
#              - Calculate and display their sum.
# - The OddList thread should:
#              - Extract all odd elements from the list.
#              - Calculate and display their sum.
# - Threads should run concurrently.
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

def EvenList(No):
    list_even = []
    sum_even = 0

    for i in No:
        if i % 2 == 0:
            list_even.append(i)
            sum_even = sum_even + i
     
    print("Even numbers from list are : ", list_even)
    print("Sum of Even numbers is : ", sum_even)
    
def OddList(No):
    list_odd = []
    sum_odd = 0

    for i in No:
        if i % 2 != 0:
            list_odd.append(i)
            sum_odd = sum_odd + i
     
    print("Odd numbers from list are : ", list_odd)
    print("Sum of Odd numbers is : ", sum_odd)
    
def main():
    start_time = time.time()

    Value = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Value):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread (target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread (target=OddList, args=(Data,), name="OddList")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()

    print("time required :",end_time-start_time)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output 
# Enter the number of elements : 6
# Enter the elements : 
# 1
# 2
# 3
# 4
# 5
# 6
# Even numbers from list are :  [2, 4, 6]
# Sum of Even numbers is :  12
# Odd numbers from list are :  [1, 3, 5]
# Sum of Odd numbers is :  9
# time required : 4.685734272003174