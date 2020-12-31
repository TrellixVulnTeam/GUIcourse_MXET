from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("RadioButton")
root.iconbitmap("../images/me.jpg")

# variable r is different from python variable
r=IntVar()
# we are setting the default checked radio button
r.set(2)

def clicked(value):
    global label
    label.forget()
    label = Label(root, text=value)
    label.pack()

r1=Radiobutton(root,text="radio_one",variable=r,value=1,command=lambda :clicked(r.get()),padx=10,pady=10)
r2=Radiobutton(root,text="radio_two",variable=r,value=2,command=lambda :clicked(r.get()),padx=10,pady=10)
r1.pack()
r2.pack()
label=Label(root,text=r.get())
label.pack()

root.mainloop()




from tkinter import *
from PIL import ImageTk,Image

# root=Tk()
# root.title("RadioButton")
# root.iconbitmap("../images/me.jpg")
#
# MODES=[
#     ("Peporoni","Peporoni"),
#     ("Assst","Assst"),
#     ("Tkinter","Tkinter"),
#     ("100days","100days"),
# ]
#
# pizza = StringVar
# # pizza.set("")
#
# def clicked(value):
#     global label
#     label.forget()
#     root.forget()
#     label = Label(root, text=value)
#     label.pack()
#
# for items,value in MODES:
#     Radiobutton(root,text=items,variable=pizza,value=value).pack(anchor=W)
#
#
#
# button=Button(root,text="clciked",command=lambda :clicked(pizza.get()))
# button.pack()
# root.mainloop()