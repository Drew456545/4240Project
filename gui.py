import psutil
import tkinter as tk

def update_info():
    # Get system information using psutil
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    # Update labels with system information
    cpu_label.config(text=f"CPU Usage: {cpu_percent:.2f}%")
    memory_label.config(text=f"Memory Usage: {memory.percent:.2f}%")

    # Schedule the update every 1 second
    root.after(1000, update_info)

# Create the main window
root = tk.Tk()
root.title("System Monitor")

# Create labels to display system information
cpu_label = tk.Label(root, text="CPU Usage: ", font=("Helvetica", 14))
memory_label = tk.Label(root, text="Memory Usage: ", font=("Helvetica", 14))
cpu_label.pack()
memory_label.pack()

# Start updating the system information
update_info()

# Run the GUI main loop
root.mainloop()
