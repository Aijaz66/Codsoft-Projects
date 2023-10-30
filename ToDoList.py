from tkinter import *
from tkinter import messagebox

def Task():
    tsk = entry.get()
    if tsk != "":
        list.insert(END, tsk)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("Error", "Please enter a task.")

def dell():
    list.delete(ANCHOR)

root = Tk()
root.geometry('500x450+500+200')
root.title('TO dO List')
root.config(bg='#223441')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.pack(pady=10)

list = Listbox(
    frame,
    width=25,
    height=8,
    font=('Arial', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)

list.pack(side=LEFT, fill=BOTH)

task = [
    'task 01',
    'task 02',
    'task 03',
    ]

for item in task:
    list.insert(END, item)

bar = Scrollbar(frame)
bar.pack(side=RIGHT, fill=BOTH)

list.config(yscrollcommand=bar.set)
bar.config(command=list.yview)

entry = Entry(
    root,
    font=('times', 24)
    )
entry.pack(pady=20)

bframe  = Frame(root)
bframe.pack(pady=20)

addTaskbuttonn = Button(
    bframe,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=Task
)
addTaskbuttonn.pack(fill=BOTH, expand=True, side=LEFT)

deltaskbutton = Button(
    bframe,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=dell
)
deltaskbutton.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
