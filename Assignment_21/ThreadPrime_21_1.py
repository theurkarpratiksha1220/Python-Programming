# Design a python application that creates two threads named Prime and NonPrime.
# - Both threads should accept a list of integers.
# - The Prime thread should display all prime numbers from the list.
# - The NonPrime thread should display all non-prime numbers from the list.
# ----------------------------------------------------------------------------------------------------------------------
import threading
import time

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Prime_List(Num):
    list_prime = []

    for i in Num:
        if ChkPrime(i):
            list_prime.append(i)
     
    print("Prime numbers from the list are : ", list_prime)

def NonPrime_List(Num):
    list_NonPrime = []

    for i in Num:
        if not ChkPrime(i):
            list_NonPrime.append(i)
     
    print("Non Prime numbers from list are : ", list_NonPrime)
    
def main():
    start_time = time.time()

    Value = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Value):
        Value = int(input())
        Data.append(Value)

    print("Actual data is :", Data)

    t1 = threading.Thread (target=Prime_List, args=(Data,), name="Prime")
    t2 = threading.Thread (target=NonPrime_List, args=(Data,), name="Non-Prime")
    
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
# Enter the number of elements : 5
# Enter the elements : 
# 1
# 2
# 3
# 4
# 5
# Actual data is : [1, 2, 3, 4, 5]
# Prime numbers from the list are :  [2, 3, 5]
# Non Prime numbers from list are :  [1, 4]
# time required : 5.4589691162109375