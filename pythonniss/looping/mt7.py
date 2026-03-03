import threading

def show(name):
    for i in range(3):
        print("Hello", name)

t = threading.Thread(target=show, args=("Jitu",))
t.start()