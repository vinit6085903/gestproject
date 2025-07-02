import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

FILENAME = "skills.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Skill", "Field", "Experience Level"])

def add_skill():
    name = name_entry.get()
    skill = skill_entry.get()
    field = field_entry.get()
    level = level_entry.get()

    if not (name and skill and field and level):
        messagebox.showwarning("Warning", "Fill all fields")
        return

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, skill, field, level])
    messagebox.showinfo("Success", "✅ Skill added")
    clear_fields()

def view_skills():
    output_text.delete("1.0", tk.END)
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            output_text.insert(tk.END, "\t".join(row) + "\n")

def search_skill():
    query = simpledialog.askstring("Search", "Enter name or skill:").lower()
    output_text.delete("1.0", tk.END)
    found = False
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if query in row[0].lower() or query in row[1].lower():
                output_text.insert(tk.END, "\t".join(row) + "\n")
                found = True
    if not found:
        messagebox.showinfo("Not Found", "❌ No matching skill found.")

def delete_skill():
    target = simpledialog.askstring("Delete", "Enter name to delete:").lower()
    updated = []
    deleted = False

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0].lower() != target:
                updated.append(row)
            else:
                deleted = True

    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(updated)

    if deleted:
        messagebox.showinfo("Deleted", "🗑️ Skill deleted")
    else:
        messagebox.showinfo("Not Found", "❌ No matching name found.")

def clear_fields():
    name_entry.delete(0, tk.END)
    skill_entry.delete(0, tk.END)
    field_entry.delete(0, tk.END)
    level_entry.delete(0, tk.END)

# GUI Setup
initialize_csv()
root = tk.Tk()
root.title("Skill Development Manager")
root.geometry("750x500")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Skill").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Field").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Experience Level").grid(row=3, column=0, padx=10, pady=5)

name_entry = tk.Entry(root, width=40)
skill_entry = tk.Entry(root, width=40)
field_entry = tk.Entry(root, width=40)
level_entry = tk.Entry(root, width=40)

name_entry.grid(row=0, column=1)
skill_entry.grid(row=1, column=1)
field_entry.grid(row=2, column=1)
level_entry.grid(row=3, column=1)

tk.Button(root, text="Add Skill", width=20, command=add_skill).grid(row=4, column=0, pady=10)
tk.Button(root, text="View All", width=20, command=view_skills).grid(row=4, column=1, pady=10)
tk.Button(root, text="Search", width=20, command=search_skill).grid(row=5, column=0, pady=5)
tk.Button(root, text="Delete", width=20, command=delete_skill).grid(row=5, column=1, pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).grid(row=6, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, height=15, width=90)
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
