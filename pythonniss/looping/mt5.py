import time

def task():
    for i in range(5):
        print("Task running", i)
        time.sleep(1)

task()
print("Main Finished")