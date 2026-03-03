import threading

class MyThread(threading.Thread):
    def run(self):
        print("bye",threading.current_thread().name)
        for i in range(3):
            print("Child Thread")
threading.current_thread().name="muna"
t = MyThread(name="WorkerThread")
t.start()
print("hi",threading.current_thread().name)