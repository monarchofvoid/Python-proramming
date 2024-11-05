from tkinter import *
from tkinter import messagebox
import random, string

root = Tk()
root.geometry("380x420")
root.title("Password Generator")
root.attributes("-toolwindow", 1)
root.resizable(width=FALSE, height=FALSE)

# intro text
title = StringVar()
label = Label(root, textvariable=title, anchor=W, pady=10).pack()
title.set("Password Strength:")

# choice part
def sel():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(root, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(root, text="EXTRA", variable=choice, value=3, command=sel).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()

# pass length information
lenlabel = StringVar()
Label(root, textvariable=lenlabel).pack()
lenlabel.set("Password length:")

# pass length number
val = IntVar()
spinlength = Spinbox(root, from_=7, to=24, textvariable=val, width=13).pack()

# callback to generate and display password
def callback():
    generated_password = passgen()
    # Show the generated password in a message box
    messagebox.showinfo("Generated Password", f"Your Password: {generated_password}")

# clickable button
passgenbutton = Button(root, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=2)
passgenbutton.pack()

# password generator function
def passgen():
    length = val.get()
    if choice.get() == 1:
        lowup = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.sample(lowup, length))
    elif choice.get() == 2:
        lowup = string.ascii_uppercase + string.ascii_lowercase
        return "".join(random.sample(lowup, length))
    elif choice.get() == 3:
        lowup = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        return "".join(random.sample(lowup, length))

root.mainloop()
