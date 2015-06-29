from tkinter import *
parent = Tk()
Label(parent, text=" Enter your Username:").pack()
Entry(parent, width=30).pack()
Label(parent, text=" Enter your Password:").pack()
Entry(parent, width=30).pack()
Button(parent, text="Search").pack()
Entry(parent, width=30).pack()
parent.mainloop()
