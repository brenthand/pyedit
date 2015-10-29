#https://www.daniweb.com/programming/software-development/code/431567/a-simple-tix-tkinter-editor
#http://knowpapa.com/text-editor/

import tkinter.tix as tix
import tkinter.scrolledtext as tkst
from tkinter import messagebox
import tkinter.filedialog as tkdf

root = tix.Tk()
textpad = tkst.ScrolledText(root, width=100, height=60)

def newfile():
    print("dummy")

def openfile():
    print("dummy")

def savefile():
    file = tkdf.asksaveasfile(mode="w", defualtextension=".txt")
    if file != None:
        text = self.textpad.get("1.0", END+"-1c")
        file.write(test)
        file.close()

def closefile():
    if messagebox.askokcancel("Quit", "Do you really want to quit"):
        root.destroy()

def about():
    print("dummy")

menu = tix.Menu(root)
root.config(menu=menu)
filemenu = tix.Menu(menu)
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="new", command=newfile)
filemenu.add_command(label="open", command=openfile)
filemenu.add_command(label="new", command=savefile)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=closefile)

helpmenu = tix.Menu(menu)
menu.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="about", command=about)


textpad.pack()
root.mainloop()
