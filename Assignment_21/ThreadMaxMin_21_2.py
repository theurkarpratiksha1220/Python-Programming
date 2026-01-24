# Design a python application that creates two threads.
# - Thread 1 should calculate and display the maximum element from an list.
# - Thread 2 should calculate and display the minimum element from the same list.
# - The list should be accepted from the user.
# ----------------------------------------------------------------------------------------------------------------------
import threading
import time

def Max_List(Num):
    Maximum_No = max(Num)
     
    print("Maximum element from an list is  : ", Maximum_No)

def Min_List(Num):
    Minimum_No = min(Num)
     
    print("Minimum element from an list is  : ", Minimum_No)
    
def main():
    start_time = time.time()

    Value = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Value):
        Value = int(input())
        Data.append(Value)

    print("Actual data is :", Data)

    t1 = threading.Thread (target=Max_List, args=(Data,), name="Max")
    t2 = threading.Thread (target=Min_List, args=(Data,), name="Min")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()

    print("time required :",end_time-start_time)

if __name__ == "__main__":
    main()


# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter the number of elements : 4
# Enter the elements : 
# 1
# 6
# 7
# 2
# Actual data is : [1, 6, 7, 2]
# Maximum element from an list is  :  7
# Minimum element from an list is  :  1
# time required : 7.004026889801025