import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

FILENAME = "crime_reports.csv"

# Some sample IPC data
IPC_SECTIONS = {
    "Theft": "IPC 378: Punishment for theft",
    "Murder": "IPC 302: Punishment for murder",
    "Assault": "IPC 351: Assault",
    "Kidnapping": "IPC 363: Punishment for kidnapping",
    "Cheating": "IPC 420: Cheating and dishonestly inducing delivery of property"
}

# Ensure file exists
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Crime Type", "Description", "Location", "IPC Section"])

# Add report
def add_report():
    name = name_entry.get()
    crime = crime_type_entry.get()
    desc = description_entry.get()
    location = location_entry.get()
    ipc = IPC_SECTIONS.get(crime, "Not Found")

    if not (name and crime and desc and location):
        messagebox.showwarning("Error", "Please fill all fields.")
        return

    with open(FILENAME, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, crime, desc, location, ipc])

    messagebox.showinfo("Success", "✅ Crime Report Added!")
    clear_entries()

# View reports
def view_reports():
    output_text.delete("1.0", tk.END)
    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            output_text.insert(tk.END, "\t".join(row) + "\n")

# Search report
def search_report():
    query = simpledialog.askstring("Search", "Enter name or crime type:").lower()
    output_text.delete("1.0", tk.END)
    found = False

    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            if query in row[0].lower() or query in row[1].lower():
                output_text.insert(tk.END, "\t".join(row) + "\n")
                found = True

    if not found:
        messagebox.showinfo("Not Found", "❌ No matching record.")

# Clear entries
def clear_entries():
    name_entry.delete(0, tk.END)
    crime_type_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)

# Initialize GUI
initialize_file()
root = tk.Tk()
root.title("Crime Prevention & IPC Reference System")
root.geometry("800x500")

# Labels and entries
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Crime Type (e.g., Theft)").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Description").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Location").grid(row=3, column=0, padx=10, pady=5, sticky='w')

name_entry = tk.Entry(root, width=40)
crime_type_entry = tk.Entry(root, width=40)
description_entry = tk.Entry(root, width=40)
location_entry = tk.Entry(root, width=40)

name_entry.grid(row=0, column=1, padx=10, pady=5)
crime_type_entry.grid(row=1, column=1, padx=10, pady=5)
description_entry.grid(row=2, column=1, padx=10, pady=5)
location_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Submit Report", width=20, command=add_report).grid(row=4, column=0, pady=10)
tk.Button(root, text="View All Reports", width=20, command=view_reports).grid(row=4, column=1, pady=10)
tk.Button(root, text="Search", width=20, command=search_report).grid(row=5, column=0, pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).grid(row=5, column=1, pady=5)

# Output text area
output_text = tk.Text(root, height=15, width=90)
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
