import tkinter as tk

parent=tk.Tk()
parent.title("Spin box")
parent.geometry('300x300')
text_var=tk.DoubleVar()
spin_box = tk.Spinbox(parent,from_=0.6,to=50.0,increment=.01,textvariable=text_var)

spin_box.pack()
parent.mainloop()
