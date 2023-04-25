# 31) Write a Python GUI program to create a window and disable to resize the window using tkintermodule.
import tkinter as tk
parent =tk.Tk()
parent.title("Welcome Shagun")
parent.resizable(0,0)
parent.mainloop()
