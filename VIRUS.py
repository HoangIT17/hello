from tkinter import *
from tkinter import messagebox

def click():
    while True:
     messagebox.showwarning(title="WARNING",message= "The computer is VIRUS")


wd=Tk()

bt=Button(wd,text="Click Me",command=click)
bt.pack()

wd.mainloop()


