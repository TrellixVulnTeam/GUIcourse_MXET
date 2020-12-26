from tkinter import *

root=Tk()
root.title("Simple Calculator")

entry=Entry(root,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def onButtonClicked(number):
    entry.insert(len(entry.get()),number)
def onButtonClearClicked():
    entry.delete(0,END)
def onAddbuttonClicked():
    first_number=entry.get()
    global f_num
    global math
    math="add"
    f_num =int(first_number)
    entry.delete(0,END)

def equalbuttonclicked():
    second_number=entry.get()
    entry.delete(0,END)
    if math == "add":
        entry.insert(0,f_num+int(second_number))
    if math == "sub":
        entry.insert(0,f_num-int(second_number))
    if math == "mul":
        entry.insert(0,f_num*int(second_number))
    if math == "div":
        entry.insert(0,f_num/int(second_number))


def onsubtractbuttonClicked():
    first_number = entry.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    entry.delete(0, END)


def onmultiplybuttonClicked():
    first_number = entry.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    entry.delete(0, END)

def ondividebuttonClicked():
    first_number = entry.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    entry.delete(0, END)


# define  buttons for calculator
button_1=Button(root,text="1",padx=40,pady=5,command=lambda :onButtonClicked(1))
button_2=Button(root,text="2",padx=40,pady=5,command=lambda :onButtonClicked(2))
button_3=Button(root,text="3",padx=40,pady=5,command=lambda :onButtonClicked(3))
button_4=Button(root,text="4",padx=40,pady=5,command=lambda :onButtonClicked(4))
button_5=Button(root,text="5",padx=40,pady=5,command=lambda :onButtonClicked(5))
button_6=Button(root,text="6",padx=40,pady=5,command=lambda :onButtonClicked(6))
button_7=Button(root,text="7",padx=40,pady=5,command=lambda :onButtonClicked(7))
button_8=Button(root,text="8",padx=40,pady=5,command=lambda :onButtonClicked(8))
button_9=Button(root,text="9",padx=40,pady=5,command=lambda :onButtonClicked(9))
button_0=Button(root,text="0",padx=40,pady=5,command=lambda :onButtonClicked(0))

button_add=Button(root,text="+",padx=90,pady=5,command=onAddbuttonClicked)
button_clear=Button(root,text="clear",padx=30,pady=5,command=onButtonClearClicked)
button_equal=Button(root,text="=",padx=90,pady=5,command=equalbuttonclicked)
button_subtract=Button(root,text="-",padx=40,pady=5,command=onsubtractbuttonClicked)
button_multiply=Button(root,text="*",padx=40,pady=5,command=onmultiplybuttonClicked)
button_divide=Button(root,text="/",padx=40,pady=5,command=ondividebuttonClicked)


# add the buttom to screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=5,column=0)
button_multiply.grid(row=4,column=1)
button_divide.grid(row=4,column=2)
button_equal.grid(row=6,column=1,columnspan=2)
button_clear.grid(row=6,column=0)




root.mainloop()
