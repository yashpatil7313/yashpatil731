import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x300")  # Set a bigger window size
root.configure(bg="black")  # Background color

# Define time update function
def time():
    string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %B %d, %Y')
    time_label.config(text=string)
    date_label.config(text=date_string)
    time_label.after(1000, time)

# Clock Label
time_label = tk.Label(root, font=('DS-Digital', 80), background='black', foreground='cyan')
time_label.pack(pady=10)

# Date Label
date_label = tk.Label(root, font=('Helvetica', 24), background='black', foreground='white')
date_label.pack()

# Start the clock
time()
root.mainloop()
