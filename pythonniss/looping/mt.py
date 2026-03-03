import tkinter as tk
import time

def download_file():
    status_label.config(text="Downloading...")
    time.sleep(5)   # Simulate long task
    status_label.config(text="Download Complete!")

root = tk.Tk()
root.title("Without Threading")

btn = tk.Button(root, text="Download", command=download_file)
btn.pack(pady=10)

status_label = tk.Label(root, text="Idle")
status_label.pack()

root.mainloop()