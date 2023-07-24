import psutil
import tkinter as tk
from tkinter import ttk, messagebox

def update_info():
    # Get system information using psutil
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
    top_processes = sorted(processes, key=lambda p: p.info['cpu_percent'], reverse=True)[:10]

    # Update labels with system information
    cpu_label.config(text=f"CPU Usage: {cpu_percent:.2f}%")
    memory_label.config(text=f"Memory Usage: {memory.percent:.2f}%")

    # Update process information
    process_listbox.delete(0, tk.END)  # Clear existing items
    for process in top_processes:
        process_info = f"PID: {process.info['pid']}, Name: {process.info['name']}, CPU: {process.info['cpu_percent']:.2f}%, Memory: {process.info['memory_percent']:.2f}%"
        process_listbox.insert(tk.END, process_info)

def refresh_info():
    update_info()
    update_network()

def kill_process():
    selected_index = process_listbox.curselection()
    if selected_index:
        selected_process = process_listbox.get(selected_index)
        pid = int(selected_process.split(":")[1].split(",")[0].strip())
        try:
            process = psutil.Process(pid)
            process.terminate()
            messagebox.showinfo("Process Terminated", f"Process with PID {pid} has been terminated.")
        except psutil.NoSuchProcess:
            messagebox.showerror("Process Not Found", "Process with the selected PID was not found.")
    else:
        messagebox.showwarning("No Process Selected", "Please select a process from the list.")

def update_network():
    # Get real-time network usage
    net_io = psutil.net_io_counters()
    upload_speed = net_io.bytes_sent / 1024  # Convert to KB
    download_speed = net_io.bytes_recv / 1024  # Convert to KB
    upload_label.config(text=f"Upload: {upload_speed:.2f} KB/s")
    download_label.config(text=f"Download: {download_speed:.2f} KB/s")

def show_process_details(event):
    selected_index = process_listbox.curselection()
    if selected_index:
        selected_process = process_listbox.get(selected_index)
        pid = int(selected_process.split(":")[1].split(",")[0].strip())
        try:
            process = psutil.Process(pid)
            process_details = f"Process ID: {process.pid}\n"
            process_details += f"Name: {process.name()}\n"
            process_details += f"Status: {process.status()}\n"
            process_details += f"CPU Usage: {process.cpu_percent(interval=0.5)}%\n"
            process_details += f"Memory Usage: {process.memory_percent()}%\n"
            process_details += f"Username: {process.username()}\n"
            process_details += f"Executable: {process.exe()}\n"
            messagebox.showinfo("Process Details", process_details)
        except psutil.NoSuchProcess:
            messagebox.showerror("Process Not Found", "Process with the selected PID was not found.")

# Create the main window
root = tk.Tk()
root.title("System Monitor")

# Create a notebook widget (tabs)
notebook = ttk.Notebook(root)

# Create the first tab for system monitor information
monitor_tab = ttk.Frame(notebook)
notebook.add(monitor_tab, text="System Monitor")
notebook.pack(fill=tk.BOTH, expand=True)

# Create labels to display system and process information
cpu_label = tk.Label(monitor_tab, text="CPU Usage: ", font=("Helvetica", 14))
memory_label = tk.Label(monitor_tab, text="Memory Usage: ", font=("Helvetica", 14))
process_label = tk.Label(monitor_tab, text="Top Processes: ", font=("Helvetica", 12), justify=tk.LEFT)
cpu_label.pack()
memory_label.pack()
process_label.pack()

# Create a listbox to display top processes with a scroll bar
process_scrollbar = tk.Scrollbar(monitor_tab, orient=tk.VERTICAL)
process_listbox = tk.Listbox(monitor_tab, font=("Helvetica", 12), height=10, yscrollcommand=process_scrollbar.set)
process_scrollbar.config(command=process_listbox.yview)
process_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
process_listbox.pack()

# Create a button to kill the selected process
kill_button = tk.Button(monitor_tab, text="Kill Process", font=("Helvetica", 12), command=kill_process)
kill_button.pack()

# Create a button to manually refresh system monitor information
refresh_button = tk.Button(monitor_tab, text="Refresh", font=("Helvetica", 12), command=refresh_info)
refresh_button.pack()

# Create labels to display network usage
upload_label = tk.Label(monitor_tab, text="Upload: ", font=("Helvetica", 12))
download_label = tk.Label(monitor_tab, text="Download: ", font=("Helvetica", 12))
upload_label.pack()
download_label.pack()

# Update initial system and network information
update_info()
update_network()

# Bind double click event to show process details
process_listbox.bind("<Double-Button-1>", show_process_details)

# Create the second tab for system information
sys_info_tab = ttk.Frame(notebook)
notebook.add(sys_info_tab, text="System Information")
notebook.pack(fill=tk.BOTH, expand=True)

# Display additional system information
sys_info_label = tk.Label(sys_info_tab, text="Additional System Information", font=("Helvetica", 14))
sys_info_label.pack()

# Get more detailed system information using psutil
cpu_info = f"Logical CPUs: {psutil.cpu_count(logical=True)}\n"
cpu_freq = psutil.cpu_freq()
cpu_info += f"CPU Frequency: {cpu_freq.current:.2f} MHz\n"
ram_info = f"Total RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB\n"

# Create labels to display the detailed system information
cpu_info_label = tk.Label(sys_info_tab, text=cpu_info, font=("Helvetica", 12), justify=tk.LEFT)
ram_info_label = tk.Label(sys_info_tab, text=ram_info, font=("Helvetica", 12), justify=tk.LEFT)
cpu_info_label.pack()
ram_info_label.pack()

# Run the GUI main loop
root.mainloop()
