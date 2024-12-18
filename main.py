from tkinter import *
from tkinter import ttk
from random import randint

def generate():
    label1.config(text=randint(int(cb1.get()), int(cb2.get())))

root = Tk()
root.geometry("200x100")
root.title("Random number")
label1 = Label(text=0)
label1.pack()
cb1 = ttk.Combobox(values=[-200, -100, 0, 100, 200])
cb1.pack()
cb2 = ttk.Combobox(values=[-200, -100, 0, 100, 200])
cb2.pack()
button = Button(text="Generate", command=generate)
button.pack()
root.mainloop()