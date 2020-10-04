from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)  #by default it will vertical
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()