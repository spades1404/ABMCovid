from ABMC19.Model.model import *
from ABMC19.GUI.gui import *
from ABMC19.Visualisation.visualisation import *

#if you want gui setup
#mainWin()

#Uncomment this for manual use with no GUI

#model = covidModel(2,2,2,1)
#while model.running == True:
#    model.step()

#just visuals
startVisuals(100,100,200,5) # gridx,gridy,num agents, num infected
