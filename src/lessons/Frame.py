from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Label")
root.iconbitmap("../images/me.jpg")


frame=LabelFrame(root,text="simple frame",padx=100,pady=100)
frame.pack(padx=10,pady=10)


button1=Button(frame,text="button1")
button2=Button(frame,text="button2")

button1.grid(row=0,column=0)
button2.grid(row=1,column=1)



root.mainloop()