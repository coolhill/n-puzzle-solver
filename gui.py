from tkinter import *
from tkinter import ttk
import solver


gui = Tk()
gui.title("GUI")
gui.geometry('1200x700')


#debug and testing data untill actual data is obtainable 
def insert():
    data = 56
    text.insert(END,(data))
    text.insert(END,(solver.start))
    

b1 = Button(text = 'Graph', height = 1, width = 5)
b1.place(relx = .95, rely = .85, anchor = "c")

b2 = Button(gui, text = 'Solve', height = 1, width = 5, command =lambda:  insert())
b2.place(relx = .30, rely = .70, anchor = "c") 

text = Listbox(height = 25, width = 75)
text.place (relx = .50, rely = .30, anchor = "c")


gui.bind('<Return>')

gui.mainloop()
