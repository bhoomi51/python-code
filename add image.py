# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='Bhoomi Gandhi', font=('Calibri (Body)', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"C:\Users\sony\Desktop\bhoomi letter.png")

# here, image option is used to
# set image on button
Button(root, text='Click Me !', image=photo).pack(side=TOP)

mainloop()