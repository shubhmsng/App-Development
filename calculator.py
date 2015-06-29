from tkinter import*
root = Tk()
val1=StringVar()
val2=StringVar()

val3=StringVar()

def add(v1,v2):
    v1 = int(v1)
    v2 = int(v2)
    ad = v1 + v2
    v = str(ad)
    result.config(text=v,bg='#dfdfdf')
    
    

def mul(v1,v2):
    
    v1 = int(v1)
    v2 = int (v2)
    ad = v1 * v2
    v = str(ad)
    result.config(text=v,bg='#dfdfdf')
    
    
def sub(v1,v2):
    
    v1 = int(v1)
    v2 = int (v2)
    ad = v1 - v2
    v = str(ad)
    result.config(text=v,bg='#dfdfdf')
    
        
def div(v1,v2):
    
    v1 = int(v1)
    v2 = int (v2)
    ad = v1 / v2
    v = str(ad)
    result.config(text=v, bg='#dfdfdf')
    
result = Label(root,text="").place(x=100,y=200)
root.title("Calculator #developed by shubham singh")
root.geometry('342x280+50+60')
Label(root,relief='groove',text="Enter First Number").place(x=10,y=10,width=140)
Entry(root,relief='groove',textvariable = val1).place(x=160,y=10, width=180)
Label(root,text="Enter Second Number",relief='groove').place(x=10, y=60,width=140)
Entry(root,relief='groove',textvariable = val2).place(x=160,y=60,width=180)
Button(root,text="ADD",relief='groove', command = lambda:add(val1.get(),val2.get())).place(x = 10, y = 100,width=70)
Button(root,text="MULTIPLY",relief='groove', command = lambda:mul(val1.get(),val2.get())).place(x = 90, y = 100,width=70)
Button(root,text="SUBTRACT",relief='groove', command = lambda:sub(val1.get(),val2.get())).place(x = 170, y = 100,width=70)
Button(root,text="DIVISION",relief='groove', command = lambda:div(val1.get(),val2.get())).place(x = 250, y = 100,width=70)
Label(root,relief='groove',text="RESULT").place(x=10,y=200,width=60)
result = Label(root, bg='#dfdfdf')
result.place(x = 80, y=200, width=250)

root.mainloop()


