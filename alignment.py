from tkinter import*
root = Tk()

Button(root,text="A").pack(side=LEFT, expand = NO, fill = Y)
Button(root,text="B").pack(side=RIGHT, expand = YES, fill = BOTH)
Button(root,text="C").pack(side=TOP, expand = NO, fill = BOTH)
Button(root,text="D").pack(side=BOTTOM, expand = YES, fill = BOTH)
Button(root,text="E").pack(side=LEFT, expand = NO, fill = Y)
Button(root,text="F").pack(side=RIGHT, expand = YES, fill = Y)
Button(root,text="G").pack(side=TOP, expand = YES, fill = Y)
