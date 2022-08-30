from cProfile import label
from tkinter import *

# Were creating the main window
root = Tk()

# Creating a Label Widget
myLabel = Label(root, text="hello world!")
# Shoving it onto the screen
myLabel.pack()


root.mainloop()

