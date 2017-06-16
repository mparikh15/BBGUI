from Tkinter import *


def doNothing():
    print "okay okay I won't"

root = Tk()


## Main Menu!

optionsbar = Menu(root)
root.config(menu = optionsbar)

## sub menu for file

fileMenu = Menu(optionsbar, tearoff = 0 )
optionsbar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New Project", command = doNothing)
fileMenu.add_command(label = "New", command = doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(optionsbar, tearoff = 0)
optionsbar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)


## Toolbar!

toolbar = Frame(root, bg= "blue")

insertStuff = Button(toolbar, text = "Insert Image", command = doNothing)
insertStuff.pack(side = LEFT, padx = 2, pady = 2)
printStuff = Button(toolbar, text = "Print", command = doNothing)
printStuff.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X )  # display the toolbar and have it stretch x.

root.mainloop()
