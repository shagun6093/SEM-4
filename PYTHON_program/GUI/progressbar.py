import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
parent=tk.Tk()
parent.title("Progress Bar")
parent.geometry('300x300')
bar =Progressbar(parent, length=250,style='black.Horizontal.TProgressbar')
bar['value']=20
bar.grid(row=0,column=0)
parent.mainloop()
