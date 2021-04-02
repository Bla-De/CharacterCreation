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
            script += sm.MoveAndType(396,15,self.name)
            
        if self.farmName != "":
            script += sm.MoveAndType(396,80,self.farmName)
            
        if self.favouriteThing != "":
            script += sm.MoveAndType(396,145,self.favouriteThing)

        if self.playAsFemale:
            script += sm.MoveAndClick(206,230)

        if self.farm == 2:
            script += sm.MoveAndClick(771,130)

        if self.farm == 3:
            script += sm.MoveAndClick(771,215)

        if self.farm == 4:
            script += sm.MoveAndClick(771,300)

        if self.farm == 5:
            script += sm.MoveAndClick(771,385)

        if self.farm == 6:
            script += sm.MoveAndClick(771,470)

        if self.farm == 7:
            script += sm.MoveAndClick(771,555)

        if self.skipIntro:
            script += sm.MoveAndClick(346,500)

        return script