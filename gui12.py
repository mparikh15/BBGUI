from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo("Window Title", "Monkeys can live up to 300 years.")

answer = tkMessageBox.askquestion("Question 1", "Is this a good app?")

if answer == "yes": 
    print " :P "

root.mainloop()
