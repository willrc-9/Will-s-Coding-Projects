See [[Setup Details]] for more

Chat GPT has instructed me to try out tkinter for my GUI. I plan on implimenting this into the calculator program that I created.

The start that Chat gave me was this:
`import tkinter as tk`
`*Create the main window*`
`root = tk.Tk()`
`root.title("My first tkinter app")  *window tile*`
`root.geometry("300x200")  *w x h*
`root.mainloop() *runs the program*

`tk.Tk()` creates the window
`title()` changes the title in the title bar
`geometry()` sets the window size, in a w x h format
`mainloop()` starts a loop that keeps the window open

In **Tkinter**, an **`Entry` widget** is basically a small text box where the user can type in a single line of text (such as numbers, words, or commands).
It’s often used for things like:
- Letting a user type a number into a calculator
- Asking for a username/password
- Getting any kind of single-line input

I've learned a few new concepts.

`Label` displays text or images
`Button` runs a function when clicked
`pack()` is a geometry manager to position widgets
`command=` tells tkinter which function to call when clicked.

# And now to impliment this into the calculator...
I have loaded up the calculator code into VScode. Here is my checklist, according to ChatGPT:
**Functions**
- Click button (number)
- Clear entry
- Calculate (=)
**GUI Setup**
**Buttons**
- Set location with list, coordinate locations
