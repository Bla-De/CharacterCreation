import os
import json
from packaging.version import Version

with open('RunnerSettings.json','r') as f:
    runnerSettings = json.load(f)

xOffset = int(runnerSettings["HorizontalResolution"]) // 2 - 356
yOffset = int(runnerSettings["VerticalResolution"]) // 2 - 300

version169 = Version("1.6.9")
version = Version(runnerSettings["Version"])
if version >= version169:
	yOffset += 24

def Extra():
    return "Sleep 1\n"

def Move(x,y):
    return "MouseMove " + str(x + xOffset) + ", " + str(y + yOffset) + "\n"

def Click():
    return "Click\n" + Extra()

def MoveAndClick(x,y,amount=1):
    script = Move(x,y)

    for i in range(amount):
        script += Click()
    
    return script

def MoveAndType(x,y,text):
    script = MoveAndClick(x,y)
    script += Type(text)

    return script

def ClickAndDrag(x1,y1,x2,y2):
    return "MouseClickDrag, Left, {}, {}, {}, {}\n".format(
        str(x1 + xOffset), str(y1 + yOffset), str(x1 + xOffset + x2), str(y1 + yOffset + y2))

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

    script += "SetTitleMatchMode, RegEx\nWinActivate, ^Stardew Valley$\n#SingleInstance force\n"
    return script

def Epilog():
    script = "Esc::ExitApp" + "\n"
    script += "return"
    return script

def Run(script):

    filename = runnerSettings["WorkingDirectory"] + "CharacterScript.ahk"

    file = open(filename, "w")
    file.write(script)
    file.close()

    os.startfile(filename)