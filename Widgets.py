from tkinter import *
root = Tk()
Label(root,text="Username ").grid(row=1,sticky=W)
Label(root,text="Password ").grid(row=2,sticky=W)
Entry(root).grid(row = 1, column = 2,sticky=E)
Entry(root).grid(row = 2,column = 2,sticky=E)
Button(root,text="Login").grid(row = 3,sticky=E)
