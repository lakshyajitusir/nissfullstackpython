import threading
import time

def task():
    print("Thread State: Running")
    time.sleep(3)   # Thread goes to Blocked (sleeping)
    print("Thread Work Completed")

# 1️⃣ NEW State
t1 = threading.Thread(target=task)
print("Thread Created → NEW State")
print("Is Alive?", t1.is_alive())   # False

# 2️⃣ RUNNABLE State
t1.start()
print("Thread Started → RUNNABLE / RUNNING State")
print("Is Alive?", t1.is_alive())   # True

# 4️⃣ BLOCKED State (sleep inside task)
time.sleep(1)
print("Thread is Sleeping → BLOCKED State")

# Wait until thread completes
t1.join()

# 5️⃣ TERMINATED State
print("Thread Finished → TERMINATED State")
print("Is Alive?", t1.is_alive())   # False