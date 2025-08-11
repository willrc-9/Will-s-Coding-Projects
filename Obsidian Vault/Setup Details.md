
First we **import Tkinter** as followed:

`import tkinter as tk`

Next, we need to **create the main application menu**:

`root=tk.Tk`

Then, we need to **name the window**:

`root.title("Application_Name")`

Finally, we need to ensure that the **application window stays open**:

`root.mainloop()`

This should give us a working GUI!

# Next, I'll be adding in objects to the GUI

First, we use create a variable to become a widget, and then give it some text.
ex.
`label = tk.label(root, text = "hello tkinter!")`
or for a button...
`button = tk.Button(root, text = "Click me!!!")`
Them, using the `.pack()` command, we can allow the widget to be 1) seen on the GUI, and 2) so we can place it where we want in the GUI.
Using the example of the button above, here's an example of how the `.pack()` command works:

# `.pack()`

`button = tk.Button(root, text = "Click me!!!")`
`button.pack()`

Pack also has options that I will list here:
- **`side`** — Which side of the container to pack the widget against.  
    Options: `"top"` (default), `"bottom"`, `"left"`, `"right"`
- **`fill`** — Whether the widget should expand to fill space along an axis.  
    Options: `"x"`, `"y"`, `"both"`, or `None` (default)
- **`expand`** — If `True`, widget expands to fill any extra space in the container.
- **`padx` and `pady`** — Add padding (space) around the widget horizontally and vertically.
- **`anchor`** — Position inside the space allocated. Like `"n"`, `"e"`, `"s"`, `"w"` (north, east, south, west).

An alternative to `.pack()` is `.grid()`. `.grid()` places objects in a grid.

# `.grid()

`tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")`

This specifies that Label is going to be placed in row 0, column 0, and it sticks to the (e)ast side of its cell.

# `.place()`

Another alternative is `.place()`, which allows you to place widgets with exact coordinates.

`tn = tk.Button(root, text="Absolute position")`
`btn.place(x=50, y=50)`

`btn_rel = tk.Button(root, text="Relative position")`
`btn_rel.place(relx=0.5, rely=0.5, anchor="center")`

`btn` is placed 50 pixels from the top and 50 pixels from the left
`btn_rel` is placed in the center at 50% of the height and width of the window.


# When to use what?

| Manager    | Best for                          | Pros                         | Cons                                       |
| ---------- | --------------------------------- | ---------------------------- | ------------------------------------------ |
| `.pack()`  | Simple vertical/horizontal layout | Easy and fast                | Less precise control                       |
| `.grid()`  | Forms, tables, complex layouts    | Precise row/column placement | Can't mix with `.pack()` in same container |
| `.place()` | Exact positioning, custom layouts | Pixel-perfect control        | Harder to maintain with resizing           |
# So how do I change their sizes?

## with `.grid()`...

Changing the size of your widget is pretty simple. This is done within the creation of the widget. Here's an example:

`btn = tk.Button(root, text="Click me", width=20, height=3)
`btn.grid(row=0, column=0)`

This will change its size by pixel, so `btn` is 20 pixels wide, 3 pixels tall, and is placed in the top left corner of the window!

Using the commands `.grid_rowconfigure()` and `.grid_columnconfigure()`, you can change the sizes of the grid


## with `.place()`...

`btn = tk.Button(root, text="Fixed size")
`btn.place(x=20, y=30, width=150, height=50)

In this example, `btn` is 150 pixels wide and 50 pixels tall

Relative size can also be changed with `.place()`.

`btn.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.2)

This places the button at 10% from the left and top of the window and makes it 50% as wide and 20% as tall as the parent.
