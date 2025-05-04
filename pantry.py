from food import Food

class Pantry:
    def __init__(self):
        self.foods = []  

    def checkFoodInPantry(self, foodName):
        for item in self.foods:
            if item["food"].name == foodName:
                return True
        return False

    def addFoodExists(self, foodname, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        for item in self.foods:
            if item["food"].name == foodname:
                item["amount"] += amount
                return True

        raise ValueError("Food not found in pantry.")

    def addFoodNotExist(self, foodname, calories, carbs, protein, unit, amount):
        if self.checkFoodInPantry(foodname):
            return "Food already exists in pantry."
        
        if not all(isinstance(x, (int, float)) for x in [calories, carbs, protein]):
            raise TypeError("Please enter numeric values for calories, carbs, and protein.")

        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        food = Food()
        food.setAttributes(foodname, calories, carbs, protein, unit)
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
        itemRemoved = False
        for item in self.foods:
            if item["food"].name == foodName: 
                if float(amount) <= float(item["amount"]):
                    item["amount"] -= amount
                    itemRemoved = True

        self.removeEmptyFood()           
        return itemRemoved
    
    def removeEmptyFood(self):
        for item in self.foods:
            if item["amount"] == 0:
                self.foods.remove(item)
                return True
        return False