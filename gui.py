from tkinter import *
from tkinter import ttk
from solver import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class Application(Tk):
   
     
    def __init__(self, master):
        Tk.__init__(self, master)
        self.master = master
        self.field()


    def field(self):
        
        self.geometry("1200x700")
        self.resizable(width=False, height=False)
        
        self.b1 = Button(self, text = 'Graph', height = 1, width = 5, command = self.graphs)
        self.b1.place(relx = .95, rely = .85, anchor = "c")

        
        self.b2 = Button(self, text = 'Solve', height = 1, width = 5, command = self.insert)
        self.b2.place(relx = .30, rely = .70, anchor = "c")

        self.text = Listbox(self, height = 25, width = 75)
        self.text.place (relx = .50, rely = .30, anchor = "c")

        self.option = OptionMenu(self, '3x3', '4x4', '5x5')
        self.option.place(relx = .30, rely = .80, anchor = "c")

        self.b2 = Button(self, text = 'Shuffle', height = 1, width = 5, command = self.shuffle)
        self.b2.place(relx = .30, rely = 1.0, anchor = "c")

                                   
    def insert(self):

        self.text.insert(END, "SOLUTION:")
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
                self.text.insert(END, b)
            self.text.insert(END, "")

            
    def shuffle(self):
        q = Node([[1,   2,  3,  4],
                  [5,   6,  7,  8],
                  [9,   10, 11, 12],
                  [13, 0, 14, 15]], 4)

        shuffle(q)


    def submit(self):
        self.b1.config(state='normal')
        self.b2.config(state='normal')
        self.top.destroy()

    def graphs(self):
        self.top2 = Toplevel()
        self.top2.title("graphs")
        self.top2.geometry("300x150+30+30")
        self.top2.transient(self)
        
        self.b1.config(state='disabled')
        self.b2.config(state='disabled')
        
        self.neural = Label(self.top2, text = "Algorithm neural expander xd")
        self.neural.pack()
        self.graphButton = Button(self.top2, text="Show!", command = lambda: graph())
        self.graphButton.pack()

        #test code for graph drawing


def Gen_RandLine( length, dims=2):

    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step
        
        return lineData
    
    
def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
        return lines


def graph():
    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    
    # Fifty lines of random 3-D lines
    data = [Gen_RandLine(25, 3) for index in range(50)]
    
    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
    
    # Setting the axes properties
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')
    
    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')
    
    ax.set_zlim3d([0.0, 1.0])
    ax.set_zlabel('Z')
    
    ax.set_title('3D Test')
    
    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                       interval=50, blit=False)
    
    plt.show()
    
if __name__ == "__main__":
    gui = Application(None)
    gui.title("Solver")
    gui.mainloop()
    
   

