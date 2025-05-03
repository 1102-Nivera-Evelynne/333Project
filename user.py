from food import Food
from pantry import Pantry
from meal import Meal

class User:
    def __init__(self):
        self.name = ""
        self.panty = Pantry()
        self.food = Food()
        self.meal = Meal()

    def setName(self, name):
        if name != "":
            self.name = name
            return True
        else:
            return False
    
    def getName(self):
        return self.name
    