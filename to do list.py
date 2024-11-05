import tkinter
import random

root = tkinter.Tk()
root.config(bg="lightblue")
root.title("To Do List")
root.geometry("370x380")

tasks = []

# Create Listbox
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        display["text"] = "Please enter a task!"
    txt_input.delete(0, "end")

def delete():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()
        display["text"] = "Task deleted!"

def delete_all():
    global tasks
    tasks = []
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    display["text"] = task

def number_of_tasks():
    number_of_tasks = len(tasks)
    msg = "Number of Tasks: %s" % number_of_tasks
    display["text"] = msg

def exit():
    root.destroy()

# Create Buttons and List options
title = tkinter.Label(root, text = "To-Do-List", bg="lightyellow")
title.grid(row=0, column=0)

display = tkinter.Label(root, text = "", bg="white")
display.grid(row=1, column=0)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=2, column=0)

btn_add_task = tkinter.Button(root, text = "Add Task", fg = "black", bg = None, command = add_task)
btn_add_task.grid(row=3, column=0)

btn_delete = tkinter.Button(root, text = "Delete", fg = "black", bg = None, command = delete)
btn_delete.grid(row=4, column=0)

btn_delete_all = tkinter.Button(root, text = "Delete All", fg = "black", bg = None, command = delete_all)
btn_delete_all.grid(row=5, column=0)

btn_choose_random = tkinter.Button(root, text = "Choose Random", fg = "black", bg = None, command = choose_random)
btn_choose_random.grid(row=6, column=0)

btn_number_of_tasks = tkinter.Button(root, text = "Number of Tasks", fg = "black", bg = None, command = number_of_tasks)
btn_number_of_tasks.grid(row=7, column=0)

btn_exit = tkinter.Button(root, text = "Exit", fg = "black", bg = None, command = exit)
btn_exit.grid(row=8, column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=9)

root.mainloop()
