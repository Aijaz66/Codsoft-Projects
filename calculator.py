import tkinter as tk

cal=""

def add_to_cal(Sym):
    global cal
    cal+= str(Sym)
    result.delete(1.0, "end")
    result.insert(1.0, cal)



def evaluate():
    global cal
    try:
        cal=str(eval(cal))
        result.delete(1.0,"end")
        result.insert(1.0, cal)
    except:
        clear()
        result.delete(1.0, "end")
        result.insert(1.0, cal)


def clear():
    global cal
    cal=""
    result.delete(1.0, "end")
    pass

root=tk.Tk()
root.geometry("300x275")

result=tk.Text(root,height=2, width=16, font=("Arial",24 ))
result.grid(columnspan=5)
button1=tk.Button(root, text="1", command=lambda: add_to_cal(1), width=5, font=("Arial", 14))
button1.grid(row=2, column=1)
button2=tk.Button(root, text="2", command=lambda :add_to_cal(2), width=5, font=("Arial", 14))
button2.grid(row=2, column=2)
button3=tk.Button(root, text="3", command=lambda :add_to_cal(3), width=5, font=("Arial", 14))
button3.grid(row=2, column=3)
button4=tk.Button(root, text="4", command=lambda :add_to_cal(4), width=5, font=("Arial", 14))
button4.grid(row=3, column=1)
button5=tk.Button(root, text="5", command=lambda :add_to_cal(5), width=5, font=("Arial", 14))
button5.grid(row=3, column=2)
button6=tk.Button(root, text="6", command=lambda :add_to_cal(6), width=5, font=("Arial", 14))
button6.grid(row=3, column=3)
button7=tk.Button(root, text="7", command=lambda :add_to_cal(7), width=5, font=("Arial", 14))
button7.grid(row=4, column=1)
button8=tk.Button(root, text="8", command=lambda :add_to_cal(8), width=5, font=("Arial", 14))
button8.grid(row=4, column=2)
button9=tk.Button(root, text="9", command=lambda :add_to_cal(9), width=5, font=("Arial", 14))
button9.grid(row=4, column=3)
button0=tk.Button(root, text="0", command=lambda :add_to_cal(0), width=5, font=("Arial", 14))
button0.grid(row=5, column=2)
buttonplus=tk.Button(root, text="+", command=lambda :add_to_cal("+"), width=5, font=("Arial", 14))
buttonplus.grid(row=2, column=4)
buttonminus=tk.Button(root, text="-", command=lambda :add_to_cal("-"), width=5, font=("Arial", 14))
buttonminus.grid(row=3, column=4)
buttonmul=tk.Button(root, text="*", command=lambda :add_to_cal("*"), width=5, font=("Arial", 14))
buttonmul.grid(row=4, column=4)
buttondiv=tk.Button(root, text="/", command=lambda :add_to_cal("/"), width=5, font=("Arial", 14))
buttondiv.grid(row=5, column=4)
buttonbrac1=tk.Button(root, text="(", command=lambda :add_to_cal("("), width=5, font=("Arial", 14))
buttonbrac1.grid(row=5, column=1)
buttonbrac2=tk.Button(root, text=")", command=lambda :add_to_cal(")"), width=5, font=("Arial", 14))
buttonbrac2.grid(row=5, column=3)
buttoneq=tk.Button(root, text="=", command=lambda :evaluate(), width=11, font=("Arial", 14))
buttoneq.grid(row=6, column=3,columnspan=3)
buttonclear=tk.Button(root, text="c", command=clear, width=5, font=("Arial", 14))
buttonclear.grid(row=6, column=2)






root.mainloop()


