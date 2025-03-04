import math
import tkinter as tk
root = tk.Tk()
name_var=tk.StringVar()
root.geometry("600x400")
L1= tk.Label(root, text="Enter your name: ")
L1.grid(row=2,column=1)

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=2,column=3)
def submit():
    name=name_var.get()
    print(f"Entry is {name}")
    return split(name)
    


def split(name):
    a = name.split(" ")
   
    print(f"Your first name is {a[0]}\nand your last name is {a[1]}")
sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.grid(row=5,column=3)

root.mainloop()