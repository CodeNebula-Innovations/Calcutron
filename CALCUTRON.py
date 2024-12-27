import tkinter as tk
import math

def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def append_to_entry(text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + text)

def calculate_square_root():
    current = entry.get()
    try:
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('.', 5, 0), ('(', 5, 1), (')', 5, 2),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4),
    ('log', 4, 4), ('ln', 5, 4), ('sqrt', 5, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 20), padx=20, pady=20,
                       command=lambda t=text: append_to_entry(t) if t != '=' else evaluate_expression() if t == '=' else calculate_square_root() if t == 'sqrt' else clear_entry() if t == 'C' else append_to_entry('**') if t == '^' else append_to_entry('math.' + t + '(') if t in ['sin', 'cos', 'tan', 'log', 'ln'] else append_to_entry(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

root.mainloop()
