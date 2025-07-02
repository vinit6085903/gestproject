import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

FILENAME = "guests.csv"

# Ensure the CSV file exists
def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Mobile", "Room No", "Check-in", "Check-out"])

# Add guest
def add_guest():
    name = name_entry.get()
    mobile = mobile_entry.get()
    room = room_entry.get()
    checkin = checkin_entry.get()
    checkout = checkout_entry.get()

    if not (name and mobile and room and checkin and checkout):
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, mobile, room, checkin, checkout])

    messagebox.showinfo("Success", "✅ Guest added successfully!")
    clear_entries()

# View all guests
def view_guests():
    output_text.delete("1.0", tk.END)
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            output_text.insert(tk.END, "\t".join(row) + "\n")

# Search guest by name
def search_guest():
    search_name = simpledialog.askstring("Search", "Enter name to search:")
    if not search_name:
        return
    search_name = search_name.lower()
    found = False
    output_text.delete("1.0", tk.END)

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and search_name in row[0].lower():
                output_text.insert(tk.END, "\t".join(row) + "\n")
                found = True
    if not found:
        messagebox.showinfo("Result", "❌ Guest not found.")

# Delete guest
def delete_guest():
    delete_name = simpledialog.askstring("Delete", "Enter guest name to delete:")
    if not delete_name:
        return
    delete_name = delete_name.lower()
    updated_rows = []
    deleted = False

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() != delete_name:
                updated_rows.append(row)
            else:
                deleted = True

    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    if deleted:
        messagebox.showinfo("Deleted", "🗑️ Guest deleted successfully.")
    else:
        messagebox.showinfo("Result", "❌ Guest not found.")

# Clear all input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)
    checkin_entry.delete(0, tk.END)
    checkout_entry.delete(0, tk.END)

# GUI Setup
initialize_csv()
root = tk.Tk()
root.title("StayRegister - Hotel Guest Management System")
root.geometry("700x500")
root.config(bg="#f2f2f2")

# Labels and entries
tk.Label(root, text="Guest Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Mobile").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Room No").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Check-in Date").grid(row=3, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Check-out Date").grid(row=4, column=0, padx=10, pady=5, sticky='w')

name_entry = tk.Entry(root, width=30)
mobile_entry = tk.Entry(root, width=30)
room_entry = tk.Entry(root, width=30)
checkin_entry = tk.Entry(root, width=30)
checkout_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1, padx=10, pady=5)
mobile_entry.grid(row=1, column=1, padx=10, pady=5)
room_entry.grid(row=2, column=1, padx=10, pady=5)
checkin_entry.grid(row=3, column=1, padx=10, pady=5)
checkout_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Guest", width=15, command=add_guest).grid(row=5, column=0, pady=10)
tk.Button(root, text="View All", width=15, command=view_guests).grid(row=5, column=1, pady=10)
tk.Button(root, text="Search Guest", width=15, command=search_guest).grid(row=6, column=0, pady=5)
tk.Button(root, text="Delete Guest", width=15, command=delete_guest).grid(row=6, column=1, pady=5)
tk.Button(root, text="Exit", width=15, command=root.destroy).grid(row=7, column=0, columnspan=2, pady=10)

# Output display area
output_text = tk.Text(root, height=15, width=80)
output_text.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
