from tkinter import *

root = Tk()
root.geometry("200x200")

my_button= Button(root, text="button", width= 10 , height= 1)
my_button.pack(side= LEFT, anchor="nw", padx=5 , pady =5)
myinput = Entry(root, width = 30)
myinput.pack(side=LEFT , anchor="nw", padx=5 , pady = 5 ,fill = X , expand= True)

root.mainloop()

