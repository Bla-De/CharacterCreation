import os
import json

with open('RunnerSettings.json','r') as f:
    runnerSettings = json.load(f)

def Move(x,y):
    return "MouseMove " + str(x) + ", " + str(y) + "\n"

def Click():
    return "Click\n"

def MoveAndClick(x,y,amount=1):
    script = Move(x,y)

    for i in range(amount):
        script += Click()
    
    return script

def MoveAndType(x,y,text):
    script = MoveAndClick(x,y)
    script += Type(text)

    return script

def Type(text):
    return "Send " + text + "\n"

def ColourClick(x,y,value):
    colourWidth = 128

    pos = int((value)/100 * colourWidth)

    return MoveAndClick(x+pos,y)

def Setup():
    mouseDelay = runnerSettings["MouseDelay"]
    if mouseDelay != None:
        script = "SetMouseDelay " + str(mouseDelay) + "\n"

    script += "SetTitleMatchMode, RegEx\nWinActivate, i)^Stardew Valley$\n"
    return script

def Run(script):

    filename = runnerSettings["WorkingDirectory"] + "CharacterScript.ahk"

    file = open(filename, "w")
    file.write(script)
    file.close()

    os.startfile(filename)