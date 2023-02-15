import tkinter as tk
import tkinter.messagebox as mb
from Character import Character
import Generator
from Runner import Runner
import ScriptMaker as sm
from Entry import Entry
from Reward import Reward
#import TwitchEventHandler
import threading
import json

runner = Runner()
runner.playAsFemale = True
listbox = None
entries = []
warningShown = False
pointsThread = None

def setupPointsThread():
    threading.Thread(target=pointsThread)

def pointsThread():
    TwitchEventHandler.startChannelPointsListen()

def getSampleEntries():
    sampleEntries = []

    with open('DefaultCharacters.json','r') as f:
        defaultCharacters = json.load(f)

    for entry in defaultCharacters["Entries"]:

        sampleEntries.append(Entry(Character(entry["Character"]),Reward(entry["User"],entry["FavouriteThing"])))

    return sampleEntries

def setupRow(window,labelName,var,row, labelColumn = 0, checkBox=False, dropdown = False):

    entryColumn = labelColumn + 1

    label = tk.Label(window, text = labelName)
    label.grid(column = labelColumn, row = row, sticky = "W")

    if checkBox:
        entry = tk.Checkbutton(window,variable=var)
        entry.grid(column=entryColumn,row=row)
    elif dropdown == "farmTypes":
        entry = tk.OptionMenu(window, var, *runner.farmTypeList)
        entry.grid(column = entryColumn, row = row, columnspan = 4, sticky = "EW")
    elif dropdown == "numberCabins":
        entry = tk.OptionMenu(window, var, *runner.numberCabins)
        entry.grid(column = entryColumn, row = row)
    else:
        entry = tk.Entry(window, textvariable = var)
        entry.grid(column=entryColumn,row=row, columnspan = 4, sticky = "EW")

    return label,entry

if __name__ == '__main__':
            
    window = tk.Tk()
    window.title("BlaDe's Character Creation")
    window.minsize(250,100)
    #mb.showwarning("Warning","This will trigger an AutoHotKey script.  \nPlease ensure Stardew Valley is running and on the character creation screen.")
    

    charVar = tk.StringVar()
    nameVar = tk.StringVar()
    farmVar = tk.StringVar()
    favouriteVar = tk.StringVar()
    farmTypeVar = tk.StringVar()
    twitchVar = tk.StringVar()
    genderVar = tk.BooleanVar()
    ccVar = tk.BooleanVar()
    minesVar = tk.BooleanVar()
    cabinsVar = tk.StringVar()
    layoutVar = tk.BooleanVar()
    seedVar = tk.StringVar()

    nameVar.set(runner.name)
    farmVar.set(runner.farmName)
    favouriteVar.set(runner.favouriteThing)
    if isinstance(runner.farm,int): 
        farmTypeVar.set(runner.farmTypeList[runner.farm - 1])
    else: 
        farmTypeVar.set(runner.farm)
    genderVar.set(not runner.playAsFemale)
    ccVar.set(runner.cc)
    minesVar.set(runner.mines)
    cabinsVar.set(runner.cabins)
    layoutVar.set(runner.layout)
    seedVar.set(runner.seed)

    currentRow = 0
    nameRow = currentRow
    currentRow += 1
    farmRow = currentRow
    currentRow += 1
    favouriteRow = currentRow
    currentRow += 1
    farmTypeRow = currentRow
    currentRow += 1
    characterRow = currentRow
    currentRow += 1
    genderRow = currentRow
    currentRow += 1
    remixRow = currentRow
    currentRow += 1
    cabinsRow = currentRow
    currentRow += 1
    seedRow = currentRow
    currentRow += 1

    setupRow(window,"Name:",nameVar,nameRow)
    setupRow(window,"FarmName:",farmVar,farmRow)
    setupRow(window,"Favourite:",favouriteVar,favouriteRow)
    setupRow(window,"FarmType:",farmTypeVar,farmTypeRow, dropdown = "farmTypes")
    setupRow(window,"Character:",charVar,characterRow)
    setupRow(window,"Male:",genderVar,genderRow,checkBox=True)
    
    tk.Label(window, text = "Remix:").grid(column = 0, row = remixRow, sticky = "W")
    setupRow(window,"CC?:",ccVar,remixRow, labelColumn= 1, checkBox=True)
    setupRow(window,"Mines?:",minesVar,remixRow, labelColumn = 3, checkBox=True)
    
    tk.Label(window, text = "Layout:").grid(column = 0, row = cabinsRow, sticky = "W")
    setupRow(window,"# Cabins:", cabinsVar, cabinsRow, labelColumn = 1, dropdown = "numberCabins")
    setupRow(window,"Separate?:", layoutVar, cabinsRow, labelColumn = 3, checkBox=True)
    setupRow(window,"Seed:",seedVar,seedRow)

    def updateRunner():
        runner.name = nameVar.get()
        runner.farmName = farmVar.get()
        runner.favouriteThing = favouriteVar.get()
        runner.farm = farmTypeVar.get()
        runner.playAsFemale = not genderVar.get()
        runner.cc = ccVar.get()
        runner.mines = minesVar.get()
        runner.cabins = cabinsVar.get()
        runner.layout = cabinsVar.get()
        runner.seed = seedVar.get() 


    def generate():

        char = Character(charVar.get())

        charErrors = char.validate()
        
        errors.configure(text= "/n".join(charErrors))
        if len(charErrors) == 0:
            updateRunner()
            script = Generator.Build(runner, char)
            sm.Run(script)
            #print(script)

    def test():
        selection = listbox.curselection()
        if selection == ():
            return

        entry = entries[selection[0]]
        
        updateRunner()
        script = Generator.Build(runner, entry.character)
        print(script)

 
    def displayEntry(event):
        selection = listbox.curselection()
        if selection == ():
            return

        entry = entries[selection[0]]

        charVar.set(str(entry.character))
        favouriteVar.set(entry.reward.user)

    #def connect():
    #    TwitchEventHandler.userAuthentication(twitchVar.get())
    #    if TwitchEventHandler.isSetup():
    #        twitchStatus.configure(text = "Connected")


    button = tk.Button(window, text = "Generate", command = generate)
    button.grid(column= 0, row = currentRow, columnspan=6)
    currentRow += 1

    errors = tk.Label(window, text = "This will trigger an AutoHotKey script.  \nPlease ensure Stardew Valley is running \nand on the character creation screen.")
    errors.grid(column=0, row = currentRow, columnspan=6)
    
    currentRow += 1

    twitchToken = tk.Entry(window, textvariable = twitchVar)
    twitchToken.grid(column = 5, row = 0)

    #twitchButton = tk.Button(window, text = "Twitch Connect", command = connect)
    #twitchButton.grid(column=2, row = 1)

    twitchStatus = tk.Label(window, text = "Disconnected")
    twitchStatus.grid(column = 5, row = 2)

    listbox = tk.Listbox(window)
    listbox.grid(column=5, row = 3, rowspan=7)
    listbox.bind("<<ListboxSelect>>", displayEntry)

    entries = getSampleEntries()

    for entry in entries:
        listbox.insert(tk.END,entry)

    window.mainloop()