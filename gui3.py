from Tkinter import *

root = Tk()

one = Label(root, text = "One", bg="red", fg="white")
one.pack() ## just some normal labels
two = Label(root, text = "Two", bg="green", fg="black")
two.pack(fill = X) ## Adjusts horizontally along the x axis
three = Label(root, text = "Three", bg="blue", fg="white")
three.pack(side = LEFT, fill = Y) ## label three adjusts vertically and is left justified

root.mainloop()
