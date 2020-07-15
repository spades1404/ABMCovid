from tkinter import *
from tkinter import messagebox

from ABMC19.GUI.components import *
from ABMC19.Visualisation.visualisation import *


class mainWin():

    def __init__(self):
        self.main = Tk()
        self.main.title("ABM CoViD-19 - Config Panel")


        genLabel(self,"Grid Height").grid(column = 0, row = 0)
        genLabel(self, "Grid Width").grid(column = 0, row = 1)
        genLabel(self, "Number of Agents").grid(column = 0, row = 2)
        genLabel(self, "# Initially Infected Agents").grid(column=0, row=3)

        self.gridHeight = genTxtBox(self)
        self.gridHeight.grid(column = 1, row = 0)
        self.gridWidth = genTxtBox(self)
        self.gridWidth.grid(column = 1, row = 1)
        self.numAgents = genTxtBox(self)
        self.numAgents.grid(column = 1, row = 2)
        self.numInfectedAgents = genTxtBox(self)
        self.numInfectedAgents.grid(column = 1, row = 3)

        genButt(self,"Run Simulation!",self.activate).grid(column = 0, row = 4, columnspan = 2)

        #genButt(self, "Run Simulation!")
        self.main.mainloop()

    def activate(self):
        try:
            h = int(self.gridHeight.get(0.0,"end"))
            w = int(self.gridWidth.get(0.0,"end"))
            a = int(self.numAgents.get(0.0,"end"))
            i = int(self.numInfectedAgents.get(0.0,"end"))
            self.main.destroy()
            startVisuals(int(h), int(w), int(a), int(i))
        except:
            messagebox.showwarning("Error","You have not entered numbers into all the boxes")


