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


