from tkinter import *
from tkinter.ttk import *

# creating Tk window
master = Tk()

# setting geometry of tk window
master.geometry("200x200")

# button widget
b1 = Button(master, text="Click me !")
b1.place(relx=1, x=-2, y=2, anchor=NE)
b1.pack(fill = X, expand = True, ipady = 40)   #ipady i.e green area around button

#b1.place(x=5, y=5, relwidth=1, relheight=1, width=-10, height=-10)

# label widget
l = Label(master, text="I'm a Label")
l.place(anchor=NW)

# button widget
b2 = Button(master, text="GFG")
b2.place(relx=0.5, rely=0.5, anchor=CENTER)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()