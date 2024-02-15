# imports the python module tkinter to be reference as "tk" throughout the program
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import os

# creates a tkinter window to be referenced as "sgt" throughout the program
sgt = Tk()

# outlines some basic styling for the window, title and icon and size
sgt.title("Student Grade Tracker") 
sgt.iconbitmap("./img/iceburg.ico")
sgt.configure(bg="#FAF9F6")
sgt.maxsize(630, 420)
sgt.minsize(630, 420)

def addClass():
    messagebox.showinfo("Message", "Click Okay to Proceed")

def selected_item():
    for i in listbox.curselection():
        return listbox.get(i)

def loadClass():
    className = selected_item()
    frameTitle.set(className)
    tabControl = ttk.Notebook(gradeViewer, width=380)

    average = ttk.Frame(tabControl) 
    hsl = ttk.Frame(tabControl)
    overview = ttk.Frame(tabControl) 

    tabControl.add(average, text ='Averages') 
    tabControl.add(hsl, text ='Highest / Lowest')
    tabControl.add(overview, text ='Overview') 
    tabControl.grid(row=1, column=0, padx=5)

sidebar = Frame(sgt, width=200, height=400)
sidebar.grid(row=0, column=0, padx=(10, 5), pady=10)
sidebar.grid_propagate(False)

text = Label(sidebar, text="Student Grade Tracker", font=("Helvetica", 12))
text.grid(row=0, column=0, columnspan=2)

text = Label(sidebar, text="Classes", font=("Helvetica", 9))
text.grid(row=1, column=0, columnspan=2)

listbox = Listbox(sidebar, width=31, height=19)
listbox.grid(row=2, column=0, padx=5, columnspan=2)

for values in os.listdir("./data"):
    listbox.insert(END, values)

text = Button(sidebar, text="Add Class", font=("Helvetica", 9), command=addClass)
text.grid(row=3, column=0, pady=5)

text = Button(sidebar, text="Load Class", font=("Helvetica", 9), command=loadClass)
text.grid(row=3, column=1, pady=5)

gradeViewer = Frame(sgt, width=400, height=400)
gradeViewer.grid(row=0, column=1, padx=(5, 10), pady=10)
gradeViewer.grid_propagate(False)

frameTitle = StringVar()
frameTitle.set("Please Select A Class From The List...")

classText = Label(gradeViewer, textvariable=frameTitle, font=("Helvetica", 12))
classText.grid(row=0, column=0)

# starts the main loop of the window
sgt.mainloop()