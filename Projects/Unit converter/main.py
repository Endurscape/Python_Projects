import math
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Unit converter")
value=tk.StringVar()
root.geometry("600x400")
lab= tk.Label(root,text="Unit convereter")
lab.grid(row=0, column=0)
input_label= tk.Label(root, text="Enter Value : ")
input_label.place(x=80,y=25)

value_entry = tk.Entry(root,textvariable = value, font=('calibre',10,'normal'), bd=2)
value_entry.place(x=160,y=25)
dic = {
    # Length conversions
    ("Kilometres", "Metres"): 1000,
    ("Metres", "Kilometres"): 0.001,
    ("Metres", "Centimetres"): 100,
    ("Centimetres", "Metres"): 0.01,
    ("Kilometres", "Miles"): 0.621371,
    ("Miles", "Kilometres"): 1.60934,
    ("Feet", "Metres"): 0.3048,
    ("Metres", "Feet"): 3.28084,
    ("Inches", "Centimetres"): 2.54,
    ("Centimetres", "Inches"): 0.393701,
    ("Feet", "Inches"):12,
    ("Inches", "Feet"):1/12,

    # Weight conversions
    ("Kilograms", "Grams"): 1000,
    ("Grams", "Kilograms"): 0.001,
    ("Kilograms", "Pounds"): 2.20462,
    ("Pounds", "Kilograms"): 0.453592,
    ("Ounces", "Grams"): 28.3495,
    ("Grams", "Ounces"): 0.035274,

    # Time conversions
    ("Hours", "Minutes"): 60,
    ("Minutes", "Seconds"): 60,
    ("Seconds", "Minutes"): 1/60,
    ("Minutes", "Hours"): 1/60,
    
    
}
unique_units = sorted(set(unit for pair in dic.keys() for unit in pair)) 
fro_label=tk.Label(root,text="From")
fro_label.place(x=120,y=55)
fro = ttk.Combobox(state="readonly", values=unique_units)
fro.place(x=160, y=55)
to = ttk.Combobox( state="readonly", values=unique_units)
to.place(x=160, y=85)
to_label=tk.Label(root,text="To")
to_label.place(x=120,y=85)


result_label=tk.Label(root,text="")
result_label.place(x=170,y=165)
def convert():
    from_unit=fro.get()
    to_unit=to.get()
    try:
        if((from_unit,to_unit) in dic):
            value_entered=float(value.get())
            factor = dic[(from_unit, to_unit)]
            result=f"Result : {round(value_entered*factor,3)} {to_unit}"
            result_label.config(text=result)

        elif (from_unit==to_unit and from_unit!=""):
          result=f"Result: {value.get()} {from_unit}"
          result_label.config(text=result)
        
        elif value=="":
            result_label.config("Not Supported")

        else:
            result_label.config(text="Not Supported")
            
    except ValueError:
        print("Invalid entry")
        result_label.config(text='Invalid entry not allowed')
        

sub_btn=tk.Button(root,text = 'Submit', command = convert)
sub_btn.place(x=190,y=120)

root.mainloop()