from food import Food
from pantry import Pantry
from meal import Meal

class User:
    def __init__(self):
        self.name = ""
        self.pantry = Pantry()
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
        return self.pantry

    def checkFoodInPantry(self, foodName):
        if self.pantry.checkFoodInPantry(foodName):
            return True
        else:
            return False
    
    def addExistingFood(self, foodname, amount):
        if self.pantry.addFoodExists(foodname, amount):
            return True
        else:
            return False
        
    def addNewFood(self, foodname, calories, carbs, protein, unit, amount):
        if self.pantry.addFoodNotExist(foodname, calories, carbs, protein, unit, amount):
            return True
        else:
            return False
    
    def removeFood(self, foodName, amount):
        if self.pantry.removeFood(foodName, amount):
            return True
        else:
            return False
    
    def createMeal(self, mealName):
        for meal in self.meals:
            if meal.getName() == mealName:
                return False
        meal = Meal()
        meal.setName(mealName)
        meal.setPantry(self.pantry)
        self.meals.append(meal)
        return True
    
    def addFoodToMeal(self, mealName, foodName, amount):
        currentMeal = None
        for meal in self.meals:
            if meal.getName() == mealName:
                    currentMeal = meal

        if currentMeal is None:
            return "Meal not found."

        if(currentMeal.addFood(foodName, amount)):
            return True
        else:
            return False
        
    def getMeal(self, mealName):
        for meal in self.meals:
            if meal.getName() == mealName:
                return meal
        return None
    
    def removeMeal(self, mealName):
        currentMeal = None
        for meal in self.meals:
            if meal.getName() == mealName:
                currentMeal = meal
        
        if currentMeal is None:
            return "Meal not found."

        for food in currentMeal.foods:
            foodName = food["food"].name
            amount = food["amount"]
            
            if self.pantry.checkFoodInPantry(foodName):
                self.pantry.addFoodExists(foodName, amount)
            else:
                self.pantry.addFoodNotExist(foodName, food["food"].calories, food["food"].carbs, food["food"].protein, food["food"].unit, amount)

        self.meals.remove(currentMeal)
        return True