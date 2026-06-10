import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

# Weight Input
weight_label = tk.Label(
    root,
    text="Weight (kg):",
    font=("Arial", 12)
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20
)
weight_entry.pack(pady=5)

# Height Input
height_label = tk.Label(
    root,
    text="Height (m):",
    font=("Arial", 12)
)
height_label.pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20
)
height_entry.pack(pady=5)

# Calculate Button
calculate_btn = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    command=calculate_bmi
)
calculate_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    fg="blue"
)
result_label.pack()

# Run Application
root.mainloop()