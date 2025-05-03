from pantry import Pantry

class Meal:
    def __init__(self):
        self.pantry = Pantry()
        self.name = ""
        self.foods = []
        self.calories = 0
        self.carbs = 0
        self.protein = 0

    def setName(self, name):
        if name != "":
            self.name = name
            return True
        else:
            return False
    
    def addFood(self, foodName, amount):
        if self.pantry.removeFood(foodName, amount):
            food = self.pantry.getFood(foodName)
            if food:
                self.foods.append({"food": food, "amount": amount})
                self.calculateNutritionalValues()
                return True
    
    def calculateNutritionalValues(self):
        for item in self.foods:
            self.calories = self.calories + (item["food"].calories * item["amount"])
            self.carbs = self.carbs + (item["food"].carbs * item["amount"])
            self.protein = self.protein + (item["food"].protein * item["amount"])

        return self.calories, self.carbs, self.protein
            
    def getMeal(self):
        meal_info = {
            "name": self.name,
            "foods": [{"food": item["food"].name, "amount": item["amount"]} for item in self.foods],
            "calories": self.calories,
            "carbs": self.carbs,
            "protein": self.protein
        }
        return meal_info
    
    def resetMeal(self):
        self.foods = []
        self.calories = 0
        self.carbs = 0
        self.protein = 0
        return True