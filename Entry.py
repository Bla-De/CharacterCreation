class Entry():
    def __init__(self,character,reward):
        self.character = character
        self.reward = reward

    def __str__(self):
        string = ""
        if self.reward != None:
            string = str(self.reward)
        if self.character != None:
            
            string += (" " if string != "" else "") + str(self.character)
        return string