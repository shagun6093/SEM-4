# 33) Write a Python GUI program to create a Text widget using tkinter module. Insert a string at thebeginning then insert a string into the current text. Delete the fi rst and last character of the text.

import tkinter as tk
parent= tk.Tk()
mytext=tk.Text(parent)
#inserting at beginning
mytext.insert('1.0','- Hello how are you -')
#inserting a string into current text
mytext.insert('1.19','I am fine, ')
#delete first and last character
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()
