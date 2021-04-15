import tkinter as tk
import tkinter.messagebox as mb
from Character import Character
import Generator
from Runner import Runner
import ScriptMaker as sm
from Entry import Entry
from Reward import Reward
import TwitchEventHandler

runner = Runner()
runner.playAsFemale = True
listbox = None
entries = []
warningShown = False

def getSampleEntries():
    sampleEntries = []

    sampleEntries.append(Entry(Character("1, 18, 1, 1, 1,0, 1, 2, 24, 25, 26, 97, 98, 99"),Reward("123","User1")))
    sampleEntries.append(Entry(Character("5, 18, 3, 2, 1,0, 1, 2, 24, 25, 26, 97, 98, 99"),Reward("234","BlaDe")))

    return sampleEntries

def setupRow(window,labelName,var,row):

    labelColumn = 0
    entryColumn = labelColumn + 1

    label = tk.Label(window, text = labelName)
    label.grid(column = labelColumn, row = row)

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

    nameVar.set(runner.name)
    farmVar.set(runner.farmName)
    favouriteVar.set(runner.favouriteThing)
    farmTypeVar.set(runner.farm)

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

    setupRow(window,"Name:",nameVar,nameRow)
    setupRow(window,"FarmName:",farmVar,farmRow)
    setupRow(window,"Favourite:",favouriteVar,favouriteRow)
    setupRow(window,"FarmType:",farmTypeVar,farmTypeRow)
    setupRow(window,"Character:",charVar,characterRow)

    def updateRunner():
        runner.name = nameVar.get()
        runner.farmName = farmVar.get()
        runner.favouriteThing = favouriteVar.get()
        runner.farm = farmTypeVar.get()

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


    button = tk.Button(window, text = "Generate", command = generate)
    button.grid(column= 0, row = currentRow, columnspan=2)
    currentRow += 1

    errors = tk.Label(window, text = "This will trigger an AutoHotKey script.  \nPlease ensure Stardew Valley is running \nand on the character creation screen.")
    errors.grid(column=0, row = currentRow, columnspan=2)
    
    currentRow += 1

    listbox = tk.Listbox(window)
    listbox.grid(column=2, row = 0, rowspan=10)
    listbox.bind("<<ListboxSelect>>", displayEntry)

    entries = getSampleEntries()

    for entry in entries:
        listbox.insert(tk.END,entry)

    window.mainloop()