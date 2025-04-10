from food import Food

class Pantry:
    def __init__(self):
        self.foods = []  
        self.foodName = ""

    def checkFoodInPantry(self, foodName):
        self.foodName = foodName
        for item in self.foods:
            if item["food"].name == foodName:
                return True
        return False

    def addFoodExists(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        for item in self.foods:
            if item["food"].name == self.foodName:
                item["amount"] += amount
                return True

        raise ValueError("Food not found in pantry.")

    def addFoodNotExist(self, calories, carbs, protein, unit, amount):
        if not all(isinstance(x, (int, float)) for x in [calories, carbs, protein]):
            raise TypeError("Please enter numeric values for calories, carbs, and protein.")

        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        food = Food()
        food.setAttributes(self.foodName, calories, carbs, protein, unit)
        self.foods.append({"food": food, "amount": amount})
        return True
    
    def getFood(self, foodName):
        for item in self.foods:
            if item["food"].name == foodName:
                return item["food"]
        return None
    
    def getFoodAmount(self, foodName):
        for item in self.foods:
            if item["food"].name == foodName:
                return item["amount"]
        return None
    
    def removeFood(self, foodName, amount):
        for item in self.foods:
            if item["food"].name == foodName:
                if amount == item["amount"]:
                    self.foods.remove(item)
                    return True
                
                elif amount < item["amount"]:
                    item["amount"] -= amount
                    return True
                
                else:
                    return False
                
        return False
    