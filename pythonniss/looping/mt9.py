import threading
import time

def task():
    for i in range(10):
        print("Child Thread Running:", i)
        time.sleep(1)

# Create Thread
t1 = threading.Thread(target=task)

print("Starting Thread...")

# Start Thread
t1.start()

# Wait for thread to finish
t1.join()

print("Main Finished")