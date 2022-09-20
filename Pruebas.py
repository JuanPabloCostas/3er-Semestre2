from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code at codemy')

frame = LabelFrame(root, padx=50,pady=50)
frame.pack(padx=100,pady=100)

b = Button(frame, text="Dont click")
b1 = Button(frame, text="or here")
b.grid(row=0,column=0)
b1.grid(row=1,column=1)

root.mainloop()

