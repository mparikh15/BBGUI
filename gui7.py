from Tkinter import *

root = Tk()

def leftClick(event):
    print "Left"

def middleClick(event):
    print "Middle"

def rightClick(event):
    print "Right"

frame = Frame(root, width = 400, height = 300)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
