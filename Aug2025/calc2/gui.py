# -------------------
# Import math functions from math.py
# -------------------

from math import add, sub, div, mul

# -------------------
# GUI Setup
# -------------------

import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")

# -------------------
# Adding in numbers
# -------------------

def numberwidget(name, number):
    name = tk.Button(root, text = number)

#numberwidget("seven", 7)

seven = tk.Button(root, text = "7")
seven.grid(row=0,column=0, sticky='e')
#seven.grid(row=0, column=0, sticky="e")



root.mainloop()
