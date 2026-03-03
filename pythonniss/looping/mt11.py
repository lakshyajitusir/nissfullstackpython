import threading
import time

def task():
    print("Child: Running")
    time.sleep(2)
    print("Child: Finished")

t1 = threading.Thread(target=task)

print("Main: Starting Child")
t1.start()

print("Main: Sleeping 1 second")
time.sleep(1)

print("Main: Awake")

t1.join()
print("Main: Finished")