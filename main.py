# imports the python module tkinter to be reference as "tk" throughout the program
import tkinter as tk

# creates a tkinter window to be referenced as "sgt" throughout the program
sgt = tk.Tk()

# outlines some basic styling for the window, title and icon
sgt.title("Student Grade Tracker") 
sgt.iconbitmap("./img/iceburg.ico")

# starts the main loop of the window
sgt.mainloop()
