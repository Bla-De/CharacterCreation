import json
import ScriptMaker as sm

class Character():
        
    def populate(self,text):
        if text == "":
            return
        row = text.split(',')
        if len(row) >= 1:
            self.skin = int(row[0])
        if len(row) >= 2:
            self.hair = int(row[1])
        if len(row) >= 3:
            self.shirt = int(row[2])
        if len(row) >= 4:
            self.pants = int(row[3])
        if len(row) >= 5:
            self.acc = int(row[4])
        if len(row) >= 6:
            self.eyeH = int(row[5])
        if len(row) >= 7:
            self.eyeS = int(row[6])
        if len(row) >= 8:
            self.eyeL = int(row[7])
        if len(row) >= 9:
            self.hairH = int(row[8])
        if len(row) >= 10:
            self.hairS = int(row[9])
        if len(row) >= 11:
            self.hairL = int(row[10])
        if len(row) >= 12:
            self.pantsH = int(row[11])
        if len(row) >= 13:
            self.pantsS = int(row[12])
        if len(row) >= 14:
            self.pantsL = int(row[13])
        if len(row) >= 15:
            self.animal = int(row[14])


    def __init__(self,text):
        self.skin = 1
        self.hair = 1
        self.shirt = 1
        self.pants = 1
        self.acc = 1
        self.eyeH = 0
        self.eyeS = 0
        self.eyeL = 0
        self.hairH = 0
        self.hairS = 0
        self.hairL = 0
        self.pantsH = 0
        self.pantsS = 0
        self.pantsL = 0
        self.animal = 1

        self.populate(text)

    def validate(self):
        
        with open('Parameters.json','r') as f:
            parameters = json.load(f)
        #Retuns array of properties that have errored
        error = []
        if not parameters["SkinMin"] <= self.skin <= parameters["SkinMax"]:
            error.append("Skin")
        if not parameters["HairMin"] <= self.hair <= parameters["HairMax"]:
            error.append("Hair")
        if not parameters["ShirtMin"] <= self.shirt <= parameters["ShirtMax"]:
            error.append("Shirt")
        if not parameters["PantsMin"] <= self.pants <= parameters["PantsMax"]:
            error.append("Pants")
        if not parameters["AccessoryMin"] <= self.acc <= parameters["AccessoryMax"]:
            error.append("Accessory")
        if not parameters["AnimalMin"] <= self.animal <= parameters["AnimalMax"]:
            error.append("Animal")

        if not parameters["HSLMin"] <= self.eyeH <= parameters["HSLMax"]:
            error.append("Eye Hue")
        if not parameters["HSLMin"] <= self.eyeS <= parameters["HSLMax"]:
            error.append("Eye Saturation")
        if not parameters["HSLMin"] <= self.eyeL <= parameters["HSLMax"]:
            error.append("Eye Lightness")

        if not parameters["HSLMin"] <= self.hairH <= parameters["HSLMax"]:
            error.append("Hair Hue")
        if not parameters["HSLMin"] <= self.hairS <= parameters["HSLMax"]:
            error.append("Hair Saturation")
        if not parameters["HSLMin"] <= self.hairL <= parameters["HSLMax"]:
            error.append("Hair Lightness")

        if not parameters["HSLMin"] <= self.pantsH <= parameters["HSLMax"]:
            error.append("Pants Hue")
        if not parameters["HSLMin"] <= self.pantsS <= parameters["HSLMax"]:
            error.append("Pants Saturation")
        if not parameters["HSLMin"] <= self.pantsL <= parameters["HSLMax"]:
            error.append("Pants Lightness")

        return error

    def makeScript(self,female = True):
        #Assumes validation has passed
        script = ""

        if self.animal > 1:
            script += sm.MoveAndClick(586,215,self.animal-1)

        if self.skin > 1:
            script += sm.MoveAndClick(236,290,self.skin-1)

        workingHair = self.hair
        if female:
            workingHair += 74 - 17
            workingHair = workingHair % 74 + 1

        if workingHair > 1:
            script += sm.MoveAndClick(236,360,workingHair-1)

        if self.shirt > 1:
            script += sm.MoveAndClick(236,430,self.shirt-1)

        if self.pants > 1:
            script += sm.MoveAndClick(236,500,self.pants-1)

        if self.acc > 1:
            script += sm.MoveAndClick(236,570,self.acc-1)

        colourLeft = 425

        script += sm.ColourClick(colourLeft,274,self.eyeH) + sm.ColourClick(colourLeft,294,self.eyeS) + sm.ColourClick(colourLeft,314,self.eyeL)
        script += sm.ColourClick(colourLeft,342,self.hairH) + sm.ColourClick(colourLeft,362,self.hairS) + sm.ColourClick(colourLeft,382,self.hairL)
        script += sm.ColourClick(colourLeft,412,self.pantsH) + sm.ColourClick(colourLeft,432,self.pantsS) + sm.ColourClick(colourLeft,452,self.pantsL)

        return script

    def __str__(self):
        return f'{self.skin}, {self.hair}, {self.shirt}, {self.pants}, {self.acc}, {self.eyeH}, {self.eyeS}, {self.eyeL}, {self.hairH}, {self.hairS}, {self.hairL}, {self.pantsH}, {self.pantsS}, {self.pantsL}, {self.animal}'

if __name__ == '__main__':

    char = Character("1, 18, 1, 1, 1,0, 1, 2, 24, 25, 26, 97, 98, 99, 5")

    error = char.validate()

   # print(error)
   
    script = sm.Setup() + char.makeScript()

    sm.Run(script)