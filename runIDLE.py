'''
_____/\\\\\\\\\______/\\\\\\\\\\\\\_____/\\\\____________/\\\\_________/\\\\\\\\\_
 ___/\\\\\\\\\\\\\___\/\\\/////////\\\__\/\\\\\\________/\\\\\\______/\\\////////__
  __/\\\/////////\\\__\/\\\_______\/\\\__\/\\\//\\\____/\\\//\\\____/\\\/___________
   _\/\\\_______\/\\\__\/\\\\\\\\\\\\\\___\/\\\\///\\\/\\\/_\/\\\___/\\\_____________
    _\/\\\\\\\\\\\\\\\__\/\\\/////////\\\__\/\\\__\///\\\/___\/\\\__\/\\\_____________
     _\/\\\/////////\\\__\/\\\_______\/\\\__\/\\\____\///_____\/\\\__\//\\\____________
      _\/\\\_______\/\\\__\/\\\_______\/\\\__\/\\\_____________\/\\\___\///\\\__________
       _\/\\\_______\/\\\__\/\\\\\\\\\\\\\/___\/\\\_____________\/\\\_____\////\\\\\\\\\_
        _\///________\///___\/////////////_____\///______________\///_________\/////////__19 #IDLE FILE
'''

#IDLE AND PYCHARM HANDLE ROOT DIR DIFFERENTLY SO THIS IS THE IDLE FOLDER

from ABMC19.Model.model import *
from ABMC19.GUI.gui import *
from ABMC19.Visualisation.visualisation import *
from ABMC19.batchrun import batchRun
import sys
import asyncio

if sys.version_info[1] == 8:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  #This handles an error that occurs only with python 3.8




#if you want gui setup
#mainWin()

#Uncomment this for manual use with no GUI

#model = covidModel(2,2,2,1)
#while model.running == True:
#    model.step()

#just visuals
startVisuals() # gridx,gridy,num agents, num infected

#batchRunning
#batchRun()
