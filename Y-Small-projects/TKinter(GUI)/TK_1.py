from tkinter import *
from webbrowser import *


def Linkedin1():
    webbrowser="http://www.youtube.com"
    webbrowser.open("http://www.youtube.com", new=1) 


def ExitFunc():
    exit()


myFrame = Tk()
myFrame.title("First APPLICATION")
myFrame.geometry("500x400")
mybutton= Button(myFrame,text="Exit Program" , foreground="#eac736", background="#eac736", padx= 10, pady =7 , command=ExitFunc)
mybutton1= Button(myFrame,text="login to Youtube" , foreground="#674ea7", background="#674ea7" , padx=30 , pady= 20 , command=Linkedin1)
mybutton1.pack()
mybutton.pack()
myFrame.mainloop()

