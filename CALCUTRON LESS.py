import tkinter as tk
import math

def button_click(event):
    text = event.widget.cget("text")
    current_expression = entry.get()

    if text == "=":
        try:
            result = eval(current_expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_listbox.insert(tk.END, f"{current_expression} = {result}")
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Division by zero")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sqrt":
        try:
            result = math.sqrt(float(current_expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_listbox.insert(tk.END, f"sqrt({current_expression}) = {result}")
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Invalid input")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    'sqrt', 'sin', 'cos', 'tan',
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 20))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

history_listbox = tk.Listbox(root, height=6, width=35)
history_listbox.grid(row=row_val, column=0, columnspan=5)
history_listbox.configure(font=('Arial', 14))

root.mainloop()
