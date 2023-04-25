# 30) Write a Python GUI program to create a label and change the label font style (font name, bold,size) using tkinter module
import tkinter as tk
parent =tk.Tk()
parent.title("Welcome Shagun")
my_label=tk.Label(parent,text="hello",font=("Arial Bold",70))
my_label.grid(row=0,column=0)
parent.mainloop()
