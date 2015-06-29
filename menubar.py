from tkinter import *
root = Tk()

showlen = BooleanVar()
theme = IntVar()

root.geometry('650x480+50+50')
root.title("My Notepad")
root.wm_iconbitmap('Notepad++.ico')
root.configure(background='#e2ffff')

# create a toplevel menu
menubar = Menu(root)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New  ", accelerator='Ctrl+N')
filemenu.add_command(label="Open...  ", accelerator='Ctrl+O')
filemenu.add_command(label="Save  ",accelerator='Ctrl+S')
filemenu.add_command(label="Save As...  ")
filemenu.add_separator()
filemenu.add_command(label="Page Setup...  ")
filemenu.add_command(label="Print...  ",accelerator='Ctrl+P')
filemenu.add_separator()
filemenu.add_command(label="Exit  ")
menubar.add_cascade(label="File  ",menu=filemenu)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo",accelerator='Ctrl+Z')
editmenu.add_separator()
editmenu.add_command(label="Cut",accelerator='Ctrl+X')
editmenu.add_command(label="Copy",accelerator='Ctrl+C')
editmenu.add_command(label="Paste",accelerator='Ctrl+V')
editmenu.add_command(label="Delete",accelerator='Del')
editmenu.add_separator()
editmenu.add_command(label="Find...",accelerator='Ctrl+F')
editmenu.add_command(label="Find Next",accelerator='F3')
editmenu.add_command(label="Replace...",accelerator='Ctrl+H')
editmenu.add_separator()
editmenu.add_command(label="Select All",accelerator='Ctrl+A')
menubar.add_cascade(label="Edit",menu=editmenu)

formatmenu = Menu(menubar,tearoff=0)
formatmenu.add_command(label="Word Wrap ")
formatmenu.add_command(label="Font ")
menubar.add_cascade(label="Format",menu=formatmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_checkbutton(label="Show Status Bar  ",variable=showlen)

themesmenu = Menu(viewmenu, tearoff=0)
themesmenu.add_radiobutton(label="Defualt Skyblue", variable=theme)
themesmenu.add_radiobutton(label="White", variable=theme)
themesmenu.add_radiobutton(label="Light Blue", variable=theme)
themesmenu.add_radiobutton(label="Light Green", variable=theme)
themesmenu.add_radiobutton(label="Light Red", variable=theme)
viewmenu.add_cascade(label="Themes  ", menu=themesmenu)
menubar.add_cascade(label="View",menu=viewmenu)



helpbar=Menu(menubar, tearoff=0)
helpbar.add_command(label="View Help ")
helpbar.add_command(label="About My Notepad")
menubar.add_cascade(label="Help",menu=helpbar)


root.config(menu=menubar)

