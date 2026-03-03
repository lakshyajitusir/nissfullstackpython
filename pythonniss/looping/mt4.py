import tkinter as tk
from tkinter import ttk
import time

def download_task():
    status_label.config(text="Downloading...")
    
    for i in range(101):
        time.sleep(0.05)   # Simulate work
        progress["value"] = i
        percent_label.config(text=f"{i}%")
        root.update_idletasks()  # Force UI update
    
    status_label.config(text="Download Complete!")

root = tk.Tk()
root.title("Without Multithreading")
root.geometry("350x200")

progress = ttk.Progressbar(root, length=250, mode="determinate", maximum=100)
progress.pack(pady=20)

percent_label = tk.Label(root, text="0%")
percent_label.pack()

btn = tk.Button(root, text="Start Download", command=download_task)
btn.pack(pady=10)

status_label = tk.Label(root, text="Idle")
status_label.pack()

root.mainloop()