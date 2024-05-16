import json
import ScriptMaker as sm

with open('RunnerSettings.json','r') as f:
    runnerSettings = json.load(f)

class Runner():

    def __init__(self):
        self.version = runnerSettings["Version"]
        self.name = runnerSettings["Name"]
        self.farmName = runnerSettings["FarmName"]
        self.favouriteThing = runnerSettings["FavouriteThing"]
        self.farm = runnerSettings["FarmType"]
        self.playAsFemale = runnerSettings["PlayAsFemale"]
        self.skipIntro = runnerSettings["SkipIntro"]
        
        self.cc = runnerSettings["remixCC"] if "remixCC" in runnerSettings else False
        self.mines = runnerSettings["remixMines"] if "remixMines" in runnerSettings else False
        self.cabins = runnerSettings["cabinCount"] if "cabinCount" in runnerSettings else "0"
        self.layout = runnerSettings["cabinLayout"] if "cabinLayout" in runnerSettings else False
        self.seed = runnerSettings["Seed"] if "Seed" in runnerSettings else ""
        
        self.farmTypeList = ["Standard", "Riverland", "Forest", "Hill-top", "Wilderness", "Four Corners", "Beach", "Meadowlands"]
        self.numberCabins = ["0", "1", "2", "3", "4", "5", "6", "7"]

        self.legacy = runnerSettings["Legacy"]

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
            
        if isinstance(self.farm,int): 
            offset = self.farm - 1
        else: 
            offset = self.farmTypeList.index(self.farm)

        if offset: 
            horizontalOffset = 1
            if self.version == "1.6":
                horizontalOffset = offset // 6 + 1
                offset = offset % 6

            script += sm.MoveAndClick(671 + 100 * horizontalOffset,45 + 85*offset)

        if self.skipIntro:
            script += sm.MoveAndClick(346,500)

        return script
    
    def advancedSettings(self):
        if self.version != "1.5" and self.version != "1.6":
            return ""
        script = ""
        script += sm.MoveAndClick(-10,600)
        
        if self.cc: 
            script += sm.ClickAndDrag(206,230,0,40)
            
        if self.mines: 
            script += sm.ClickAndDrag(206,430,0,40)
            
        script += sm.MoveAndClick(781,515,7)
        
        if self.cabins != "0":
            script += sm.ClickAndDrag(206, 230, 0, 40*int(self.cabins))
            
            if self.layout: 
                script += sm.ClickAndDrag(206,290,0,40)
                
        script += sm.MoveAndClick(236,500)
        script += "Send {BackSpace 10} \n"
        
        if self.seed != "":
            if len(self.seed) <= 9:
                script += sm.MoveAndType(236,500,self.seed)
            else:
                script += "Clipboard := " + self.seed[1:] + " \n"
                script += sm.Type(self.seed[0])
                script += "SendInput ^v" + " \n"

        if self.legacy:
            script += sm.MoveAndClick(781,515,1)
            script += sm.MoveAndClick(16,500)
            script += sm.MoveAndClick(236,430)

        
        return script