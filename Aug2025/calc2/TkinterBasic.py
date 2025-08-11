import tkinter as tk

def say_hello():
    label.config(text = "hello tkinter")

# Create the main window
root = tk.Tk()
root.title("Hello app") #window tile
root.geometry("300x200") # w x h

label = tk.Label(root, text="Click the button below.")
label.pack(pady=20)

button = tk.Button(root, text = "Say hello", command = say_hello)
button.pack(pady=20)

root.mainloop()
