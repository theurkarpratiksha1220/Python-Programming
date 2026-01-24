# Design a python application that creates three threads named Small, Capital and Digits.
# - All threads should accept a string as input.
# - The Small thread should count and display the number of lowercase characters.
# - The Capital thread should count and display the number of uppercase characters.
# - The Digits thread should count and dispkay the number of numeric digits.
# - Each thread must also display:
#     - Thread ID
#     - Thread Name
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

def Small_Lowercase(s):
    count = 0
    for char in s:
        if char.islower():
            count = count + 1

    thread = threading.current_thread()
    print("Thread Id : ", thread.ident)
    print("Thread Name : ", thread.name)

    print("Count of Lowercase Characters is: ", count)

def Capital_Uppercase(s):
    count = 0
    for char in s:
        if char.isupper():
            count = count + 1

    thread = threading.current_thread()
    print("Thread Id : ", thread.ident)
    print("Thread Name : ", thread.name)

    print("Count of Lowercase Characters is: ", count)

def Digits_Numbers(s):
    count = 0
    for char in s:
        if char.isdigit():
            count = count + 1
    thread = threading.current_thread()
    print("Thread Id : ", thread.ident)
    print("Thread Name : ", thread.name)

    print("Count of Lowercase Characters is: ", count)

def main():

    start_time = time.time()

    Value = input("Enter any String: ")

    # Create threads
    t1 = threading.Thread(target=Small_Lowercase, args=(Value,), name="Small")
    t2 = threading.Thread(target=Capital_Uppercase, args=(Value,), name="Capital")
    t3 = threading.Thread(target=Digits_Numbers, args=(Value,), name="Digits")

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to complete
    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()

    print("time required :",end_time-start_time)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Enter any String: abcd67ABHCYT
# Thread Id :  6144159744
# Thread Name :  Small
# Count of Lowercase Characters is:  4
# Thread Id :  6160986112
# Thread Name :  Capital
# Count of Lowercase Characters is:  6
# Thread Id :  6177812480
# Thread Name :  Digits
# Count of Lowercase Characters is:  2
# time required : 11.207895040512085