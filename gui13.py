from Tkinter import *

root = Tk()

def DeleteShit():
    canvas.delete(blackLine, redLine)

def DeleteALL():
    canvas.delete(ALL)


canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill = "red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")

button = Button(root, text = "Delete shit", command = DeleteShit)
button.pack()

destroy = Button(root, text = "DESTROY", command = DeleteALL)
destroy.pack()

root.mainloop()
