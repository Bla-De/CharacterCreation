import tkinter as tk
from Character import Character
import Generator
from Runner import Runner
import ScriptMaker as sm

runner = Runner()
runner.playAsFemale = True

def getSampleCharacters():
    characters = []

    characters.append(Character("1, 18, 1, 1, 1,0, 1, 2, 24, 25, 26, 97, 98, 99"))
    characters.append(Character("5, 18, 3, 2, 1,0, 1, 2, 24, 25, 26, 97, 98, 99"))

    return characters

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Python Tkinter Text Box")
    window.minsize(600,400)

    name = tk.StringVar()
    nameEntered = tk.Entry(window, width = 50, textvariable = name)
    nameEntered.grid(column = 0, row = 1)

    def clickMe():
        char = Character(name.get())

        charErrors = char.validate()
        
        errors.configure(text= "/n".join(charErrors))
        if len(charErrors) == 0:
            script = Generator.Build(runner, char)
            sm.Run(script)

 
    label = tk.Label(window, text = "Enter Character")
    label.grid(column = 0, row = 0)

    button = tk.Button(window, text = "Click Me", command = clickMe)
    button.grid(column= 0, row = 2)

    errors = tk.Label(window, text = "Errors")
    errors.grid(column=0, row = 3)

    window.mainloop()