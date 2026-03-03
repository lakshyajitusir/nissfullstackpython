import threading

def display():
    for i in range(5):
        print("Child Thread")

t = threading.Thread(target=display)
t.start()
for i in range(5):
        print("main Thread")
