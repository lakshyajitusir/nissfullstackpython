import tkinter as tk
from tkinter import ttk
import threading
import time

def download_task():
    for i in range(101):
        time.sleep(0.05)  # Simulate work
        root.after(0, update_progress, i)

def update_progress(value):
    progress["value"] = value
    percent_label.config(text=f"{value}%")
    if value == 100:
        status_label.config(text="Download Complete!")

def start_download():
    status_label.config(text="Downloading...")
    thread = threading.Thread(target=download_task)
    thread.start()

root = tk.Tk()
root.title("Progress Bar Example")
root.geometry("350x200")

progress = ttk.Progressbar(root, length=250, mode="determinate", maximum=100)
progress.pack(pady=20)

percent_label = tk.Label(root, text="0%")
percent_label.pack()

btn = tk.Button(root, text="Start Download", command=start_download)
btn.pack(pady=10)

status_label = tk.Label(root, text="Idle")
status_label.pack()

root.mainloop()