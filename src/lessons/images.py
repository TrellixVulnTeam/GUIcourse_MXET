from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image tutorial")
root.iconbitmap("../images/me.jpg")



my_image1=ImageTk.PhotoImage(Image.open("../images/me.jpg"))
my_image2=ImageTk.PhotoImage(Image.open("../images/breakfast.png"))
my_image3=ImageTk.PhotoImage(Image.open("../images/breakfast2.png"))
my_image4=ImageTk.PhotoImage(Image.open("../images/dinner.png"))
my_image5=ImageTk.PhotoImage(Image.open("../images/lunch1.png"))
my_image6=ImageTk.PhotoImage(Image.open("../images/snacks.png"))

my_images=[my_image1,my_image2,my_image3,my_image4,my_image5,my_image6]





my_label=Label(image=my_images[1])
my_label.grid(row=0, column=0,columnspan=3)
# my_label.pack()
# my_label.grid(row=0, column=0, columnspan=3)
def forward():
    return

def backs():
    return



button_back=Button(root,text="<<",command=lambda :backs())
button_forward=Button(root,text=">>",command= lambda :forward())
btton_quit=Button(root,text="Exit program",command=root.quit,padx=50,pady=10)
btton_quit.grid(row=1,column=1)
button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)


root.mainloop()


# from tkinter import *
# from PIL import ImageTk,Image
#
# root=Tk()
# root.title("image tutorial")
# root.iconbitmap("../images/bell.png")
#
# my_image=ImageTk.PhotoImage(Image.open("../images/me.jpg"))
# mylabel=Label(image=my_image)
# mylabel.pack()
#
# button=Button(root,text="quit",command=root.quit)
# button.pack()
#
# root.mainloop()
