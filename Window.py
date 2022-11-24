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

def setupRow(window,labelName,var,row,checkBox=False):

    labelColumn = 0
    entryColumn = labelColumn + 1

    label = tk.Label(window, text = labelName)
    label.grid(column = labelColumn, row = row)

    if checkBox:
        entry = tk.Checkbutton(window,width=20,variable=var)
        entry.grid(column=entryColumn,row=row)
    else:
        entry = tk.Entry(window, width = 20, textvariable = var)
        entry.grid(column=entryColumn,row=row)

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
    farmTypeVar = tk.IntVar()
    twitchVar = tk.StringVar()
    genderVar = tk.BooleanVar()

    nameVar.set(runner.name)
    farmVar.set(runner.farmName)
    favouriteVar.set(runner.favouriteThing)
    farmTypeVar.set(runner.farm)
    genderVar.set(not runner.playAsFemale)

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

    setupRow(window,"Name:",nameVar,nameRow)
    setupRow(window,"FarmName:",farmVar,farmRow)
    setupRow(window,"Favourite:",favouriteVar,favouriteRow)
    setupRow(window,"FarmType:",farmTypeVar,farmTypeRow)
    setupRow(window,"Character:",charVar,characterRow)
    setupRow(window,"Male:",genderVar,genderRow,checkBox=True)

    def updateRunner():
        runner.name = nameVar.get()
        runner.farmName = farmVar.get()
        runner.favouriteThing = favouriteVar.get()
        runner.farm = farmTypeVar.get()
        runner.playAsFemale = not genderVar.get()

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
    button.grid(column= 0, row = currentRow, columnspan=2)
    currentRow += 1

    errors = tk.Label(window, text = "This will trigger an AutoHotKey script.  \nPlease ensure Stardew Valley is running \nand on the character creation screen.")
    errors.grid(column=0, row = currentRow, columnspan=2)
    
    currentRow += 1

    twitchToken = tk.Entry(window, textvariable = twitchVar)
    twitchToken.grid(column = 2, row = 0)

    #twitchButton = tk.Button(window, text = "Twitch Connect", command = connect)
    #twitchButton.grid(column=2, row = 1)

    twitchStatus = tk.Label(window, text = "Disconnected")
    twitchStatus.grid(column = 2, row = 2)

    listbox = tk.Listbox(window)
    listbox.grid(column=2, row = 3, rowspan=10)
    listbox.bind("<<ListboxSelect>>", displayEntry)

    entries = getSampleEntries()

    for entry in entries:
        listbox.insert(tk.END,entry)

    window.mainloop()