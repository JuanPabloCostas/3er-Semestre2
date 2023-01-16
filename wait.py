import tkinter as tk

root = tk.Tk()

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("350x350")
    new_button = tk.Button(new_window, text="Click Me!", command=new_window.destroy)
    new_button.pack()

open_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack()

root.mainloop()