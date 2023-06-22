from tkinter import *
from tkinter import messagebox
import os

# Reading file
file_path = 'todo.txt'
try:
    file = open(file_path)
except IOError:
    file = open(file_path, 'w+')
filesize = os.path.getsize("todo.txt")
print(file)
fileLines = str(file.read())
print(fileLines)
if filesize != 0:
    taskList = fileLines.split("\n")
else:
    taskList = []
print(taskList)

# Functions
def newTask():
    task = myEntry.get()
    if task != "":
        taskList.append(task)
        lb.insert(END, task)
        myEntry.delete(0, "end")
        with open("todo.txt", "w") as file:
            fileLines = "\n".join(taskList)
            file.write(fileLines)
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    task = lb.get(ACTIVE)
    if task in taskList:
        taskList.remove(task)
    lb.delete(ANCHOR)
    with open("todo.txt", "w") as file:
        fileLines = "\n".join(taskList)
        file.write(fileLines)

# Defining the tkinter

ws = Tk()
ws.geometry('400x300+100+50')
ws.title('To Do List')
ws.config(bg='#2D2D2D')
ws.resizable(width=False, height=False)

# Defining the frame

frame = Frame(ws,bg='#262626')
frame.pack(pady=5)

# Defining the "To Do List" box

lb = Listbox(
    frame,
    width=25, height=8, font=('Times', 14), bd=0, fg='#ffffff', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none", bg = "#666666"

)
lb.pack(side=LEFT, fill=BOTH)

for item in taskList:
    lb.insert(END, item)

sb = Scrollbar(frame,bg='#262626')
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

myEntry = Entry(
    ws,
    font=('times', 24), fg='#ffffff', bg = "#666666", bd=0,
    )

myEntry.pack(pady=5)

buttonFrame = Frame(ws)
buttonFrame.pack(pady=5)

addTaskBtn = Button(
    buttonFrame,
    text='Add Task', font=('times 14'), fg='#1aff1a', bg = "#666666", padx=10, pady=5, bd=0,
    command=newTask
)
addTaskBtn.grid(column = 1, row = 0)


delTaskBtn = Button(
    buttonFrame,
    text='Delete Task', font=('times 14'), fg='#ff6666', bg = "#666666", padx=10, pady=5, bd=0,
    command=deleteTask
)
delTaskBtn.grid(column = 2, row = 0)


ws.mainloop()
