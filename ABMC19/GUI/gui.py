from tkinter import *
from tkinter import messagebox

from ABMC19.GUI.components import *
from ABMC19.Visualisation.visualisation import *

from ABMC19.Visualisation.visualisation import startVisuals
from ABMC19.batchrun import batchRun

class gui():
    def __init__(self):
        self.start()
        return
    def start(self):
        main = Tk()
        main.title("ABMC19")
        genLabel(main,"Welcome! Please choose the method of running the model.",width=60).grid(column = 0, row = 0,columnspan= 2)
        genButt(main,"Run Visual", command= lambda: self.visualSetup(main)).grid(column = 0, row = 1 )
        genButt(main,"Run BatchRun (BETA)", command= lambda: self.batchSetup(main)).grid(column = 1, row = 1 )
        genLabel(main, "Created by Rajib Ahmed and Pharadon Larg - 2020", width=60,height = 1).grid(column=0, row=2,columnspan=2)
        main.mainloop()

    def removeWindow(self,x):
        x.destroy()

    def visualSetup(self,x):
        self.removeWindow(x)
        startVisuals()

    def batchSetup(self,x):
        self.removeWindow(x)

        main = Tk()

        main.title("ABMC19 - BatchRun Setup")

        genLabel(main,text = "Static Parameters",width=60).grid(column = 0, row = 0, columnspan = 2)
        genLabel(main,text = "Variable Parameter - Agent Num",width=60).grid(column = 2, row = 0, columnspan = 2)

        genLabel(main, text="Grid Size (x by x)").grid(column=0, row=1)
        genLabel(main, text="Social Distance (0 to 1)").grid(column=0, row=2)
        genLabel(main, text="Hygenic (0 to 1)").grid(column=0, row=3)
        genLabel(main, text="Essential Movement (0 to 1)").grid(column=0, row=4)
        genLabel(main, text="Masks (0 to 1)").grid(column=0, row=5)
        genLabel(main, text="Starting Infected").grid(column=0, row=6)

        #this part was coded really lazily so all the
        a = genTxtBox(main)
        b = genTxtBox(main)
        c = genTxtBox(main)
        d = genTxtBox(main)
        e = genTxtBox(main)
        f = genTxtBox(main)

        a.grid(column=1, row=1)
        b.grid(column=1, row=2)
        c.grid(column=1, row=3)
        d.grid(column=1, row=4)
        e.grid(column=1, row=5)
        f.grid(column=1, row=6)

        genLabel(main, text="Start Range").grid(column=2, row=1)
        genLabel(main, text="End Range").grid(column=2, row=2)
        genLabel(main, text="Step Num").grid(column=2, row=3)

        g = genTxtBox(main)
        h = genTxtBox(main)
        i = genTxtBox(main)

        g.grid(column=3, row=1)
        h.grid(column=3, row=2)
        i.grid(column=3, row=3)

        genLabel(main, text="Precautionary Measure", width=60).grid(column=2, row=4, columnspan=2)

        j = BooleanVar()
        x = Checkbutton(main, text = "Contact Tracing", onvalue = True, offvalue = False, variable = j)
        x.grid(column = 2,row = 5)

        k = BooleanVar()
        y = Checkbutton(main, text="Lockdown", onvalue = True, offvalue = False, variable = k)
        y.grid(column=3, row=5)

        Label(main,text =

        '''
        Standard Lockdown Parameters - 
        1. Activation Point is 100 infected
        2. Deactivation Point is 50 ticks under 100 infected
        3. 5 Iterations Per Parameter change
        '''
              ).grid(column = 2, columnspan = 2, row = 6)

        genButt(main,"Run!",command= lambda :
                self.startBatch(main,
                                a.get(0.0,"end"),
                                b.get(0.0,"end"),
                                c.get(0.0,"end"),
                                d.get(0.0,"end"),
                                e.get(0.0,"end"),
                                f.get(0.0,"end"),
                                g.get(0.0,"end"),
                                h.get(0.0,"end"),
                                i.get(0.0,"end"),
                                j.get(),
                                k.get()
                )
                ).grid(column = 0,columnspan=4,row=7)



        main.mainloop()
        return

    def startBatch(self,
                   main,
                   a,b,c,d,e,f,g,h,i,j,k):

        for i in [a,b,c,d,e,f,g,h,i]:
            try:
                int(i)
            except:
                try:
                    float(i)
                except:
                    messagebox.showwarning(message="Please enter a number or float for each box")
                    return

        if (int(h)-int(g)) % int(i) != 0 and (int(h)-int(g)) != 0:
            messagebox.showwarning(message="Please ensure that the range is divisible by the step")
            return

        if int(f)>int(g) :
            s = messagebox.askyesno(message='''
            Your starting infected is above the starting range for your agents.
            It is not recommended you do this since some of your data will be 0,
            Would you like to continue?''')

            if s == False:
                return

        self.removeWindow(main)


        batchRun(
            int(a),
            float(b),
            float(c),
            float(d),
            float(e),
            int(f),
            j,
            k,
            range(int(g),(int(h) + int(i)),int(i))
        )





        return



