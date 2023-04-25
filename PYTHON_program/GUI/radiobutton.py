import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Radiobutton
parent=tk.Tk()
parent.title("Radio Buton")
parent.geometry('300x300')
radio1 =tk.Radiobutton(parent,text="first",value=1)
radio2 =tk.Radiobutton(parent,text="second",value=2)
radio3 =tk.Radiobutton(parent,text="third",value=3)
radio1.grid(row=0,column=0)
radio2.grid(row=0,column=1)
radio3.grid(row=0,column=3)
parent.mainloop()
