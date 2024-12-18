from tkinter import *
from random import randint

def generate():
    label1.config(text=randint(0, 100))

root = Tk()
root.geometry("200x100")
root.title("Random number")
label1 = Label(text=0)
label1.pack()
button = Button(text="Generate", command=generate)
button.pack()
root.mainloop()