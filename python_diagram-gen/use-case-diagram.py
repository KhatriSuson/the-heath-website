import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


# Function to generate Use Case Diagram
def generate_use_case_diagram():
    messagebox.showinfo("Use Case Diagram", "Placeholder: Generate a Use Case Diagram here.")


# Function to generate Class Diagram
def generate_class_diagram():
    messagebox.showinfo("Class Diagram", "Placeholder: Generate a Class Diagram here.")


# Function to generate Flowchart
def generate_flowchart():
    messagebox.showinfo("Flow Chart", "Placeholder: Generate a Flow Chart here.")


# Function to generate Gantt Chart
def generate_gantt_chart():
    messagebox.showinfo("Gantt Chart", "Placeholder: Generate a Gantt Chart here.")


# Function to save a diagram
def save_diagram():
    file = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    if file:
        messagebox.showinfo("Save Diagram", f"Diagram saved at {file}")


# Main GUI window
root = tk.Tk()
root.title("Diagram Generator")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Hospital Management System Diagram Generator", font=("Arial", 14), wraplength=350)
title_label.pack(pady=10)

# Buttons for different diagrams
btn_use_case = ttk.Button(root, text="Generate Use Case Diagram", command=generate_use_case_diagram)
btn_use_case.pack(pady=10)

btn_class = ttk.Button(root, text="Generate Class Diagram", command=generate_class_diagram)
btn_class.pack(pady=10)

btn_flowchart = ttk.Button(root, text="Generate Flowchart", command=generate_flowchart)
btn_flowchart.pack(pady=10)

btn_gantt = ttk.Button(root, text="Generate Gantt Chart", command=generate_gantt_chart)
btn_gantt.pack(pady=10)

# Save button
btn_save = ttk.Button(root, text="Save Diagram", command=save_diagram)
btn_save.pack(pady=20)

# Run the application
root.mainloop()
