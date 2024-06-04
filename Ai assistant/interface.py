import tkinter as tk
import subprocess
import time
import threading

def run_text_to_speech():
    subprocess.Popen(["python", "texttospeech.py"], shell=True)
    countdown_thread = threading.Thread(target=count_down)
    countdown_thread.start()

def count_down():
    for i in range(3, 0, -1):
        countdown_label.config(text=f"Recording, {i} seconds left")
        root.update()
        time.sleep(1)
    countdown_label.config(text="Recording, 0 seconds left")

root = tk.Tk()
root.title("Text to Speech")
root.geometry("480x320")  # Set window dimensions to 480x320

countdown_label = tk.Label(root, text="Click the button to start recording")
countdown_label.pack(pady=20)

button = tk.Button(root, text="Run Text to Speech", command=run_text_to_speech)
button.pack(pady=10)

root.mainloop()
