from tkinter import *
from tkinter import ttk

root = Tk()
root.withdraw()
redvar = IntVar()
bluevar = IntVar()
greenvar = IntVar()
def returnvalues():
    getinput()
    return (redvar.get(),greenvar.get(),bluevar.get())
def getinput():
    popup = Toplevel(root)
    popup.title("Pick Color")
    red = Spinbox(popup,from_=0,to=255,textvariable=redvar)
    redtext = Label(popup,text="Red Value")
    green = Spinbox(popup,from_=0,to=255,textvariable=greenvar)
    greentext = Label(popup,text="Green Value")
    blue = Spinbox(popup,from_=0,to=255,textvariable=bluevar)
    blutext = Label(popup,text="Blue Value")
    red.grid(row=0,column=0)
    redtext.grid(row=0,column=1)
    green.grid(row=1,column=0)
    greentext.grid(row=1,column=1)
    blue.grid(column=0,row=2)
    blutext.grid(row=2,column=1)
    submit = Button(popup,text="Submit",command=popup.destroy)
    submit.grid(row=3,column=0,columnspan=2)
    popup.wait_window()