from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='GeeksforGeeks', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
img = PhotoImage(file=r"C:\Users\sony\Desktop\bhoomi letter.png")

# Resizing image to fit on button
#subsample is used to resize image
photoimage = img.subsample(3, 3)

# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Button(root, text='Click Me !', image=photoimage,
       compound=LEFT).pack(side=TOP)

mainloop()