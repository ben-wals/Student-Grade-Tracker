# imports the python module tkinter to be reference as "tk" throughout the program
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import os
import json
import statistics

# creates a tkinter window to be referenced as "sgt" throughout the program
sgt = Tk()

# outlines some basic styling for the window, title and icon and size
sgt.title("Student Grade Tracker") 
sgt.iconbitmap("./img/iceburg.ico")
sgt.configure(bg="#FAF9F6")
sgt.maxsize(630, 420)
sgt.minsize(630, 420)

def extremities(classID):
    currentHighest = 0
    assignmentNo = 0
    for i in os.listdir("./data/" + classID + "/grades"):
        with open("./data/" + classID + "/grades/" + i, "r") as f:
            gradeDict = json.loads(f.read())
            if gradeDict[max(gradeDict)] > currentHighest:
                currentHighest = gradeDict[max(gradeDict)]
                assignmentNo = i
    with open("./data/" + classID + "/grades/" + os.listdir("./data/" + classID + "/grades")[(int(assignmentNo[:-5]) - 1)], "r") as f:
        gradeDict = json.loads(f.read())
        return max(gradeDict), currentHighest, assignmentNo

def averageCalc(classID):
    overallTotal = []
    individualAverages = []
    for i in os.listdir("./data/" + classID + "/grades"):
        runningTotal = []
        with open("./data/" + classID + "/grades/" + i, "r") as f:
            gradeDict = json.loads(f.read())
            for i in gradeDict.values():
                overallTotal.append(i)
                runningTotal.append(i)
            individualAverages.append(round(statistics.mean(runningTotal), 1) )
    return round(statistics.mean(overallTotal), 1), round(statistics.median(overallTotal), 1), individualAverages, len(os.listdir("./data/" + classID + "/grades"))

def addClass():
    messagebox.showinfo("Message", "Click Okay to Proceed")

def selected_item():
    for i in listbox.curselection():
        return listbox.get(i)

def loadClass():

    if selected_item() == None:
        messagebox.showinfo("Error", "Please select a class to continue", icon="error")
        return

    className = selected_item()
    frameTitle.set(className)
    tabControl = ttk.Notebook(gradeViewer, width=380)

    overview = ttk.Frame(tabControl)
    average = ttk.Frame(tabControl) 
    hsl = ttk.Frame(tabControl)
    addGrades = ttk.Frame(tabControl)

    tabControl.add(overview, text ='Overview')
    tabControl.add(average, text ='Averages')

    overallMeanAverageValue, overallMedianAverageValue, invdividualAverageValues, assignmentQuant = averageCalc(className)
    avgHeadline = "Average accross all " + str(assignmentQuant) + " assignments:\n" + str(overallMeanAverageValue) + " (mean) " + str(overallMedianAverageValue) + " (median) "
    overallAverage = Label(average, text=avgHeadline, font=("Helvetica", 12))
    overallAverage.grid(row=0, column=0, columnspan=3)

    tabControl.add(hsl, text ='Highest / Lowest')
    tabControl.add(addGrades, text ='Add Grades') 
    tabControl.grid(row=1, column=0, padx=5)

    highestKey, highestValue, highestassignmentno = extremities(className)
    highestLowestHeadline = "The individual with the highest grade is\n" + str(highestKey) + "\nwhom in the assigment with ID " + str(highestassignmentno[:-5]) + " scored\n" + str(highestValue) + "/100"
    overallHighestLowest = Label(hsl, text=highestLowestHeadline, font=("Helvetica", 12))
    overallHighestLowest.grid(row=0, column=0, columnspan=3)

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