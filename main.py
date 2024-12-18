from tkinter import *
from tkinter import ttk, messagebox
from random import randint

def generate():
    fr = int(cb1.get())
    to = int(cb2.get())
    if fr >= to:
        messagebox.showinfo('Error', 'Wrong input')
    else:
        label1.config(text=randint(fr, to))

root = Tk()
root.geometry("200x100")
root.title("Random number")
label1 = Label(text=0)
label1.grid(row=0, column=1)
cblabel1 = Label(text="From:")
cblabel1.grid(row=1, column=0)
cb1 = ttk.Combobox(values=[-200, -100, 0, 100])
cb1.grid(row=1, column=1)
cblabel1 = Label(text="To:")
cblabel1.grid(row=2, column=0)
cb2 = ttk.Combobox(values=[-100, 0, 100, 200])
cb2.grid(row=2, column=1)
button = Button(text="Generate", command=generate)
button.grid(row=3, column=1)
root.mainloop()