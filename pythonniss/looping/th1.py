import threading
import time
def print_numbers():
    for i in range(5):
        print("Number:", i)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)

t1.start()
for i in range(5):
    print("hi")
t1.join()

print("Finished")