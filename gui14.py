from Tkinter import *

root = Tk()

photo = PhotoImage(file="test2.png")
label = Label(root, image= photo)
label.pack()

root.mainloop()
