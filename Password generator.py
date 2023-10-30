from tkinter import *
import random, string

root= Tk()
root.geometry("400x280")
root.title("Random Pass Generator")
title=StringVar()
lab=Label(root, textvariable=title).pack()
title.set("Password Strenght")

def selection():
    selection=choice.get()

choice=IntVar()
rad1=Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=CENTER)
rad2=Radiobutton(root, text="Weak", variable=choice, value=2, command=selection).pack(anchor=CENTER)
rad3=Radiobutton(root, text="Strong", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice=Label(root)
labelchoice.pack()

lenghtlab=StringVar()
lenghtlab.set("Password Length")
lengthtitle=Label(root, textvariable=lenghtlab).pack()

value=IntVar()
spinlabel=Spinbox(root, from_=9, to_=20, textvariable=value, width=13 ).pack()

def call():
    pas.config(text=genpass())

button=Button(root, text="Generate Password",bd=5,height=2,command=call,pady=3)
button.pack()
password=str(call)

pas=Label(root, text="")
pas.pack(side=BOTTOM)

poor=string.ascii_uppercase + string.ascii_lowercase
weak=string.ascii_lowercase + string.ascii_uppercase + string.digits
sym=" !@#$%^&*()"
strong=string.ascii_uppercase + string.ascii_lowercase + string.digits + sym

def genpass():
    if choice.get()==1:
        return "".join(random.sample(poor, value.get()))
    if choice.get()==2:
        return "".join(random.sample(weak, value.get()))
    if choice.get()==3:
        return "".join(random.sample(strong, value.get()))
root.mainloop()

