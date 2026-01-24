# Design a python application that creates two threads named EvenFactor and OddFactor.
# - Both threads should accept one integer number as a parameter 
# - The EvenFactor thread should:
#              - Identify all even factors of the given number.
#              - Calculate and display the sum of even factors.
# - The OddFactor thread should:
#              - Identify all odd factors of the given number.
#              - Calculate and display the sum of odd factors.
# - After both threads complete execution, the main thread should display the message: "Exit from main"
# ----------------------------------------------------------------------------------------------------------------------
import threading
import time

def EvenFactor(No):
    list_even = []
    sum_even = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            list_even.append(i)
            sum_even = sum_even + i
     
    print("Even Factors of given number are : ", list_even)
    print("Sum of Even Factors is : ", sum_even)
    
def OddFactor(No):
    list_odd = []
    sum_odd = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            list_odd.append(i)
            sum_odd = sum_odd+ i
     
    print("Odd Factors of given number are : ", list_odd)
    print("Sum of Odd Factors is : ", sum_odd)
    
def main():
    start_time = time.time()

    Value = int(input("Enter any number: "))

    t1 = threading.Thread (target=EvenFactor, args=(Value,), name="EvenFactor")
    t2 = threading.Thread (target=OddFactor, args=(Value,), name="OddFactor")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()

    print("time required :",end_time-start_time)

    print("Exit from main")

if __name__ == "__main__":
    main()


# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter any number: 12
# Even Factors of given number are :  [2, 4, 6, 12]
# Sum of Even Factors is :  24
# Odd Factors of given number are :  [1, 3]
# Sum of Odd Factors is :  4
# time required : 3.613802909851074
# Exit from main