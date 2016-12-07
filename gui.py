from tkinter import *
from tkinter import ttk

from solver import *

gui = Tk()
gui.title("GUI")
gui.geometry('1200x700')

#debug and testing data untill actual data is obtainable 
def insert():

    text.insert(END, "SOLUTION:")
    goal = [[1,   2,  3,  4],
            [5,   6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15,  0]]
    
    start = Node([[1,   2,  3,  4],
                  [5,   6,  7,  8],
                  [9,   10, 11, 12],
                  [13, 0, 14, 15]], 4)
    
    for a in a_star(start, goal, 4):
        for b in a.q:
            text.insert(END, b)
        text.insert(END, "")

    
    
b1 = Button(text = 'Graph', height = 1, width = 5)
b1.place(relx = .95, rely = .85, anchor = "c")

b2 = Button(gui, text = 'Solve', height = 1, width = 5, command =lambda:  insert())
b2.place(relx = .30, rely = .70, anchor = "c") 

text = Listbox(height = 25, width = 75)
text.place (relx = .50, rely = .30, anchor = "c")


gui.bind('<Return>')

gui.mainloop()
