from tkinter import *

master = Tk()
master.geometry("175x175")

v = StringVar(master, "1")

# Dictionary to create multiple buttons
values = {"RadioButton 1": "1",
          "RadioButton 2": "2",
          "RadioButton 3": "3",
          "RadioButton 4": "4",
          "RadioButton 5": "5"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text=text, variable=v,value=value, indicator=0,background="light blue").pack(fill=X, ipady=5)

mainloop()