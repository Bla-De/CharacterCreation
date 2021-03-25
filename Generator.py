from Runner import Runner
from Character import Character
import ScriptMaker as sm

def Build(runner,character):
    script = sm.Setup() + runner.makeScript() + character.makeScript()
    return script

if __name__ == '__main__':
    runner = Runner()

    string = "1, 18, 1, 1, 1,0, 1, 2, 24, 25, 26, 97, 98, 99"

    char = Character(string)

    script = Build(runner,char)

    sm.Run(script)


