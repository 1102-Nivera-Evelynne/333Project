from food import Food
from pantry import Pantry
from meal import Meal

class User:
    def __init__(self):
        self.name = ""
        self.panty = Pantry()
    

    def setName(self, name):
        self.name = name
        return True
    
    def getName(self):
        #test commit
        return self.name
    