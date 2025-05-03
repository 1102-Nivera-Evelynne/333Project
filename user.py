from food import Food
from pantry import Pantry
from meal import Meal

class User:
    def __init__(self):
        self.name = ""
        self.panty = Pantry()
        self.food = Food()
       # self.meal = Meal()
        self.meals = []

    def setName(self, name):
        if name != "":
            self.name = name
            return True
        else:
            return False
    
    def getName(self):
        return self.name
    
    def getPantry(self):
        return self.panty

    def checkFoodInPantry(self, foodName):
        if self.panty.checkFoodInPantry(foodName):
            return True
        else:
            return False
    
    def addExistingFood(self, amount):
        if self.panty.addFoodExists(amount):
            return True
        else:
            return False
        
    def addNewFood(self, calories, carbs, protein, unit, amount):
        if self.panty.addFoodNotExist(calories, carbs, protein, unit, amount):
            return True
        else:
            return False
    
    def removeFood(self, foodName, amount):
        if self.panty.removeFood(foodName, amount):
            return True
        else:
            return False
    
    def createMeal(self, mealName):
        self.meal.setPantry(self.panty)
        self.meal.setName(mealName)
        self.meals.append(self.meal)
        return True
    
    def addFoodToMeal(self, mealname, foodName, amount):
        for meal in self.meals:
            if meal.getName() == mealname:
                if meal.addFood(foodName, amount):
                    return True
        return False