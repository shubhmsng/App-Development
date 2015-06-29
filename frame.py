from tkinter import *

root = Tk()

Label(root,text="!!!Click on The Frame!!!!").pack()


def mycallback(event):
    print("time",event.time)
    print ("you clicked at", event.x, event.y)


myframe = Frame(root, bg='green', width=530, height=480)

myframe.bind("<Button-1>",mycallback)

myframe.pack()

root.mainloop()


