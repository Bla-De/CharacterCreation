import json
import ScriptMaker as sm

with open('RunnerSettings.json','r') as f:
    runnerSettings = json.load(f)

class Runner():

    def __init__(self):
        self.name = runnerSettings["Name"]
        self.farmName = runnerSettings["FarmName"]
        self.favouriteThing = runnerSettings["FavouriteThing"]
        self.farm = runnerSettings["FarmType"]
        self.playAsFemale = True
        self.skipIntro = True

    def makeScript(self):
        script = ""
        if self.name != "":
            script += sm.MoveAndType(1000,255,self.name)
            
        if self.farmName != "":
            script += sm.MoveAndType(1000,320,self.farmName)
            
        if self.favouriteThing != "":
            script += sm.MoveAndType(1000,385,self.favouriteThing)

        if self.playAsFemale:
            script += sm.MoveAndClick(810,470)

        if self.farm == 2:
            script += sm.MoveAndClick(1375,370)

        if self.farm == 3:
            script += sm.MoveAndClick(1375,455)

        if self.farm == 4:
            script += sm.MoveAndClick(1375,540)

        if self.farm == 5:
            script += sm.MoveAndClick(1375,625)

        if self.farm == 6:
            script += sm.MoveAndClick(1375,710)

        if self.farm == 7:
            script += sm.MoveAndClick(1375,795)

        if self.skipIntro:
            script += sm.MoveAndClick(950,740)

        return script