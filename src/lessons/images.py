from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image tutorial")
root.iconbitmap("../images/me.jpg")


my_image=ImageTk.PhotoImage(Image.open("../images/me.jpg"))
my_label=Label(image=my_image)
my_label.pack()



btton_quit=Button(root,text="quit",command=root.quit,padx=50,pady=10)
btton_quit.pack()


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
