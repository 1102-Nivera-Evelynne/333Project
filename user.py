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
        for meal in self.meals:
            if meal.getName() == mealName:
                print("Meal already exists.")
                return False
        meal = Meal()
        meal.setName(mealName)
        meal.setPantry(self.panty)
        self.meals.append(meal)
        return True
    
    def addFoodToMeal(self, mealName, foodName, amount):
        currentMeal = None
        for meal in self.meals:
            if meal.getName() == mealName:
                    currentMeal = meal

        if currentMeal is None:
            print("Meal not found.")
            return False

        if(currentMeal.addFood(foodName, amount)):
            return True
        else:
            return False
        
    def getMeal(self, mealName):
        for meal in self.meals:
            if meal.getName() == mealName:
                return meal
        return None