# Design a python application that creates two separate threads named Even and Odd.
# - The Even thread should display the first 10 even numbers.
# - The Odd thread should display the first 10 odd numbers.
# - Both threads should execute independently using the threading module.
# - Ensure proper thread creation and execution.
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

def EvenPrint():
    print("Even Numbers are : ")
    for i in range(2,21,2):
        print(i, end=' ')
    print()
    
def OddPrint():
    print("Odd Numbers are : ")
    for i in range(1,20,2):
        print(i, end=' ')
    print()
    
def main():
    start_time = time.time()

    t1 = threading.Thread (target=EvenPrint,name="Even")
    t2 = threading.Thread (target=OddPrint,name="Odd")
    
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
# Even Numbers are : 
# 2 4 6 8 10 12 14 16 18 20 
# Odd Numbers are : 
# 1 3 5 7 9 11 13 15 17 19 
# time required : 0.0002696514129638672