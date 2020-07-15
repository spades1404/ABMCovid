from tkinter import *


def genLabel(main,text):
    return Label(
        main.main,
        width = 20,
        height = 2,
        borderwidth = 1,
        text = text,
        relief = "ridge",
        bg = "black",
        fg = "white"
    )

def genButt(main,text,command):
    return Button(
        main.main,
        text = text,
        command = command,
        width = 30
    )

def genTxtBox(main):
    return Text(
        main.main,
        width = 20,
        height = 2,
        relief = "sunken",
        undo = True
    )
