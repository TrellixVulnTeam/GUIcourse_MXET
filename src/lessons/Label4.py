from tkinter import *

root=Tk()

entry=Entry(root,width=50,bg="black",fg="white")
entry.pack()
entry.insert(0,"enter tthe name plaes")

def clickedme():
    label=Label(root,text=entry.get())
    label.pack()

button=Button(root,text="Click me",padx=30,bg="#000000",fg="#ffffff",command=clickedme)
button.pack()



root.mainloop()


#
# from tkinter import *
#
# root=Tk()
#
# entry=Entry(root,bg="black",fg="white")
# entry.pack()
# entry.insert(0,"enter the name")
#
# def clicked():
#     label=Label(root,text="button clicked")
#     label.pack()
#
# button=Button(root,text="click me",fg="black",padx=30,pady=20,command=clicked)
# button.pack()
#
# root.mainloop()