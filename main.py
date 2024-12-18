from tkinter import *
from tkinter import ttk, messagebox
from random import randint

def ignore():
    n = int(entry.get())
    if n not in listbox.get(0, END):
        listbox.insert(END, n)

def generate():
    fr = int(cb1.get())
    to = int(cb2.get())
    if fr > to:
        messagebox.showinfo('Error', 'Wrong input')
    else:
        r = randint(fr, to)
        while r in listbox.get(0, END):
            r = randint(fr, to)
        randomNumber.config(text=r)

root = Tk()
root.geometry("200x250")
root.title("Random number")
randomNumber = Label(text=0)
randomNumber.grid(row=0, column=1)
Label(text="From:").grid(row=1, column=0)
cb1 = ttk.Combobox(values=[-200, -100, 0, 100])
cb1.grid(row=1, column=1)
Label(text="To:").grid(row=2, column=0)
cb2 = ttk.Combobox(values=[-100, 0, 100, 200])
cb2.grid(row=2, column=1)
Label(text="Ignore:").grid(row=3, column=0)
entry = Entry()
entry.grid(row=3, column=1)
listbox = Listbox(selectmode=EXTENDED, height=5)
listbox.grid(row=4, column=1)
button2 = Button(text="Ignore", command=ignore)
button2.grid(row=5, column=1)
button2 = Button(text="Generate", command=generate)
button2.grid(row=6, column=1)
root.mainloop()