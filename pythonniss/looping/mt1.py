import tkinter as tk
import threading
import time

def download_file():
    status_label.config(text="Downloading...")
    time.sleep(5)   # Simulate long task
    status_label.config(text="Download Complete!")

def start_download():
    thread = threading.Thread(target=download_file)
    thread.start()

root = tk.Tk()
root.title("With Threading")

btn = tk.Button(root, text="Download", command=start_download)
btn.pack(pady=10)

status_label = tk.Label(root, text="Idle")
status_label.pack()

root.mainloop()