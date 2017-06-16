from Tkinter import *


def doNothing():
    print "okay okay I won't"

root = Tk()

optionsbar = Menu(root)
root.config(menu = optionsbar)

fileMenu = Menu(optionsbar, tearoff = 0 )
optionsbar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New Project", command = doNothing)
fileMenu.add_command(label = "New", command = doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(optionsbar, tearoff = 0)
optionsbar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)


root.mainloop()
