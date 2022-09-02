from cProfile import label
from tkinter import *

# Were creating the main window
root = Tk()

def MyClick():
    myLabel = Label(root, text="Look i clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click me", command=MyClick, fg="blue", bg="#FFF")
myButton.pack()




# # Creating a Label Widget
# myLabel1 = Label(root, text="hello world!")
# myLabel2 = Label(root, text="Juan Pablo Costas")

# # Shoving it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)


root.mainloop()

