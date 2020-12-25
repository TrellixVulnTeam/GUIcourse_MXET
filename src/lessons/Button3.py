from tkinter import *

root=Tk()

def myClick():
    showlabel=Label(root,text="you clicked me")
    showlabel.pack()

mybutton=Button(root,text="click me",state=DISABLED,fg="white",bg="black")

mybutton2=Button(root,text="click me button",fg="blue",bg="#000000",padx=10,pady=10,command=myClick)


mybutton.pack()
mybutton2.pack()
root.mainloop()


# from tkinter import *
#
# root=Tk()
#
#
# def onClciked():
#
#     label=Label(root,text="clicked {}".format(100))
#     label.pack()
#
# button=Button(root,text="clickme",padx=10,pady=5,fg="white",bg="black",command=onClciked)
# button.pack()
# root.mainloop()