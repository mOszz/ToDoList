import tkinter

win = tkinter.Tk()
win.title('ToDo-List Mosz')
win.geometry("400x650")
win.resizable(0, 0)
win.configure(bg='#beffb8')
win.resizable(height = None, width  = None)




def newTask():
    task = (task_entry.get())
    listbox_tasks.insert(tkinter.END,task)

def delTask():
    task_delete = listbox_tasks.curselection()[0]
    listbox_tasks.delete(task_delete)

def saveTask():
    f = open('tasks_list.txt', 'w+')
    tasks_list = listbox_tasks.get(0, tkinter.END)
    for task in tasks_list:
        f.write(task + "\n")
        print(task)
    f.close()

def loadTask():
    f = open("tasks_list.txt", "r")
    for x in f:
        listbox_tasks.insert(tkinter.END, x)



#GUI
frame_tasks = tkinter.Frame(win)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, bg='#beffb8', borderwidth=0, highlightthickness=0, height=15, width=34, font=("Arial", 15))
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

task_entry = tkinter.Entry(win, font=("Arial", 16), width=25, borderwidth=0, highlightthickness=0)
task_entry.pack()

button_frame = tkinter.Frame(win, bg="#beffb8")
button_frame.pack(pady=10, expand=False)

add_task = tkinter.Button(button_frame, text="New Task", font=("Ubuntu", 12),borderwidth=0 ,bg="#787878", width=13, height=2, command=newTask)
add_task.grid(row=0, column=0, padx=15, pady=15)

del_task = tkinter.Button(button_frame, text="Delete Task", font=("Ubuntu", 12),borderwidth=0 ,bg="#787878", width=13, height=2, command=delTask)
del_task.grid(row=0,column=1, padx=15, pady=15)

save_task = tkinter.Button(button_frame, text="Save Tasks", font=("Ubuntu", 12),borderwidth=0 ,bg="#787878", width=13, height=2, command=saveTask)
save_task.grid(row=1,column=0)

load_task = tkinter.Button(button_frame, text="Load Tasks", font=("Ubuntu", 12),borderwidth=0 ,bg="#787878", width=13, height=2, command=loadTask)
load_task.grid(row=1,column=1)



win.mainloop()


