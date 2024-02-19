# A quick note, i went a little too ambitious with this project and wasn't able to achive full functionality as specificed in the homwork with my additional multi-assignment feature


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
    messagebox.showinfo("Please use the terminal", "Please continue in the python terminal.")
    yearGroup = input("Please enter the new classes year group\n")
    optionBlock = input("Please enter the new classes option block\n")
    Subject = input("Please enter the new classes subject\n")
    classCode = yearGroup + optionBlock.upper() + "-" + Subject[:2]
    os.mkdir("./data/" + classCode)
    students  = { "students" : [] }
    name = ""
    while name.lower() != "done":
        name = input("Please enter the name of a student in the class alternitively enter 'done' when finished\n")
        if name != "done":
            students["students"].append(name)
    with open("./data/" + classCode + "/students.json", "w") as f:
        f.write(json.dumps(students))

def selected_item():
    for i in listbox.curselection():
        return listbox.get(i)

def addGradesFunc(classID):
    with open("./data/" + classID + "/students.json", "r") as f:
            grades = {}
            studentsDict = json.loads(f.read())
            assignmentNo = len(os.listdir("./data/" + classID + "/grades")) + 1
            for i in studentsDict["students"]:
                grade = input("Enter " + i + "'s grade for assignment " + str(assignmentNo) + " :\n")
                grades[i] = grade
    with open("./data/" + classID + "/grades/" + assignmentNo + ".json", "w") as f:
        f.write(json.dumps(grades))

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

    overviewHead = Label(overview, text="Select Assignment:", font=("Helvetica", 12))
    overviewHead.grid(row=0, column=0)

    options = os.listdir("./data/" + className + "/grades")

    varList = StringVar(sgt)
    varList.set("0.json")

    overviewSelector = OptionMenu( overview , varList , *options ) 
    overviewSelector.grid(row=0, column=1)

    overviewTree = ttk.Treeview(overview, columns=('name', 'grade'), show='headings')
    overviewTree.heading('name', text='Name')
    overviewTree.heading('grade', text='Grade')
    overviewTree.grid(row=1, column=0, columnspan=3)

    def loadGrades(classID, assignment):
        for row in overviewTree.get_children():
            overviewTree.delete(row)
        with open("./data/" + classID + "/grades/" + assignment, "r") as f:
            gradeDict = json.loads(f.read())
            for key in gradeDict:
                overviewTree.insert('', END, values=(key, gradeDict[key]))
        print("Done!")

    loadAssignment = Button(overview, text="Load Assignment", font=("Helvetica", 9), command=loadGrades(className, varList.get()))
    loadAssignment.grid(row=0, column=2)

    loadGrades(className, "0.json")

    tabControl.add(average, text ='Averages')

    overallMeanAverageValue, overallMedianAverageValue, invdividualAverageValues, assignmentQuant = averageCalc(className)
    avgHeadline = "Average accross all " + str(assignmentQuant) + " assignments:\n" + str(overallMeanAverageValue) + " (mean) " + str(overallMedianAverageValue) + " (median) "
    overallAverage = Label(average, text=avgHeadline, font=("Helvetica", 12))
    overallAverage.grid(row=0, column=0, columnspan=3)

    tabControl.add(hsl, text ='Highest / Lowest')

    highestKey, highestValue, highestassignmentno = extremities(className)
    highestLowestHeadline = "The individual with the highest grade is\n" + str(highestKey) + "\nwhom in the assigment with ID " + str(highestassignmentno[:-5]) + " scored\n" + str(highestValue) + "/100"
    overallHighestLowest = Label(hsl, text=highestLowestHeadline, font=("Helvetica", 12))
    overallHighestLowest.grid(row=0, column=0, columnspan=3)

    tabControl.add(addGrades, text ='Add Grades') 
    tabControl.grid(row=1, column=0, padx=5)

    a = Button(addGrades, text="Add Grades", font=("Helvetica", 9), command=addGradesFunc(className))
    a.grid(row=0, column=0)

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