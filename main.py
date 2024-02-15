# imports the python module tkinter to be reference as "tk" throughout the program
from tkinter import *
import os

# creates a tkinter window to be referenced as "sgt" throughout the program
sgt = Tk()

# outlines some basic styling for the window, title and icon and size
sgt.title("Student Grade Tracker") 
sgt.iconbitmap("./img/iceburg.ico")
sgt.configure(bg="#FAF9F6")
sgt.maxsize(630, 420)
sgt.minsize(630, 420)

sidebar = Frame(sgt, width=200, height=400)
sidebar.grid(row=0, column=0, padx=(10, 5), pady=10)

listbox = Listbox(sidebar, width=33, height=22)
listbox.grid(row=2, column=0)

text = Label(sidebar, text="Classes", font=("Helvetica", 9))
text.grid(row=1, column=0)

text = Label(sidebar, text="Student Grade Tracker", font=("Helvetica", 12))
text.grid(row=0, column=0)

for values in os.listdir("./data"):
    listbox.insert(END, values)

gradeViewer = Frame(sgt, width=400, height=400)
gradeViewer.grid(row=0, column=1, padx=(5, 10), pady=10)

# starts the main loop of the window
sgt.mainloop()