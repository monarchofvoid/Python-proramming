from tkinter import *

class CustomButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground

# Function to update the display
def button_click(value):
    current = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, current + str(value))
    entry.config(fg="black")  # Set text color to black for user input

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
        entry.config(fg="green")  # Set text color to green for result
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
        entry.config(fg="red")  # Set text color to red for error

# Function to clear the display
def clear_display():
    entry.delete(0, END)
    entry.config(fg="black")  # Reset text color to black when cleared

# Create the main window
root = Tk()
root.resizable(False, False)
root.title("Simple Calculator")

# Create the display
entry = Entry(root, width=20, font=("Arial", 18), insertontime=0, bd=5, borderwidth=8, foreground="black", highlightthickness=1, highlightcolor="#5b8a6f", highlightbackground="#5b8a6f", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5)

# Define button layout
button_layout = [
    [("7", "#a4c3b2"), ("8", "#a4c3b2"), ("9", "#a4c3b2"), ("/", "#7a9e7e")],
    [("4", "#a4c3b2"), ("5", "#a4c3b2"), ("6", "#a4c3b2"), ("*", "#7a9e7e")],
    [("1", "#a4c3b2"), ("2", "#a4c3b2"), ("3", "#a4c3b2"), ("-", "#7a9e7e")],
    [("C", "#ff4d4d"), ("0", "#a4c3b2"), ("=", "#5b8a6f"), ("+", "#7a9e7e")]
]

# Create buttons using a loop
for r, row in enumerate(button_layout):
    for c, (text, bg_color) in enumerate(row):
        button = CustomButton(root, text=text, width=5, height=2, font=("Arial", 14), bg=bg_color, activebackground=bg_color, command=lambda value=text: button_click(value) if value not in ["=", "C"] else calculate() if value == "=" else clear_display())
        button.grid(row=r+1, column=c, padx=5, pady=5)

# Run the application
root.mainloop()
