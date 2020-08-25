from tkinter import *


def genLabel(main,
             text,
             width = 30,
             height = 2,
             bg = "black",
             fg = "white"):
    return Label(
        main,
        width = width,
        height = height,
        borderwidth = 1,
        text = text,
        relief = "ridge",
        bg = bg,
        fg = fg
    )

def genButt(main,text,command):
    return Button(
        main,
        text = text,
        command = command,
        width = 30
    )

def genTxtBox(main):
    return Text(
        main,
        width = 20,
        height = 2,
        relief = "sunken",
        undo = True
    )
