from Tkinter import *

root = Tk()   ## creates window - usuallyl use

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg = "Blue")
button3 = Button(topFrame, text="Button 3", fg = "Green")
button4 = Button(bottomFrame, text = "Button 4", fg = "Purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = RIGHT)
button4.pack(side = BOTTOM)

root.mainloop()   ## keeps the program runnning until user quits
