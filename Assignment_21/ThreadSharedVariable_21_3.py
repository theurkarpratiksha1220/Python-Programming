# Design a python application where multiple threads update a shared variable.
# - Use a Lock to avoid race conditions.
# - Each thread should increment the shared counter multiple times.
# - Display the final value of the counter after all threads complete execution.
# ----------------------------------------------------------------------------------------------------------------------

import threading
import time

# Shared variable
counter = 0

# Lock to avoid race conditions
lobj = threading.Lock()

# Function each thread will run 
def increment_counter(Notimes):
    global counter
    for _ in range(Notimes):
        with lobj:       
            counter = counter + 1

def main():
    start_time = time.time()

    num_threads = 8
    increments_per_thread = 1000
    threads = []

    # Create and start threads
    for i in range(num_threads):
        t = threading.Thread(target=increment_counter, args=(increments_per_thread,), name=f"Thread-{i+1}")
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    end_time = time.time()

    print("Final value of counter:", counter)
    print("Expected value:", num_threads * increments_per_thread)
    print("Time required:", end_time - start_time)

if __name__ == "__main__":
    main()


# ----------------------------------------------------------------------------------------------------------------------
# Output -
# Final value of counter: 8000
# Expected value: 8000
# Time required: 0.0018591880798339844