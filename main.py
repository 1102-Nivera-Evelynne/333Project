from food import Food
from meal import Meal

class Main:
    def __init__(self):
        self.meal = Meal()
        self.pantry = self.meal.pantry
        self.food = Food()

        self.insertFood()
        self.insertFood()
        self.removeFood()
        self.makeMeal()

    def insertFood(self):
        name = input("Enter food name: ")

        if self.pantry.checkFoodInPantry(name):
            amount = float(input("Enter amount to add: "))
            self.pantry.addFoodExists(amount)
        else:
            calories = float(input("Enter calories: "))
            carbs = float(input("Enter carbs: "))
            protein = float(input("Enter protein: "))
            unit = input("Enter unit: ")
            amount = float(input("Enter amount: "))
            self.pantry.addFoodNotExist(calories, carbs, protein, unit, amount)

    def removeFood(self):
        name = input("Enter food name to remove: ")
        amount = float(input("Enter amount to remove: "))
        if self.pantry.removeFood(name, amount):
            print(f"Removed {amount} of {name}.")
            print(f"Remaining amount: {self.pantry.getFoodAmount(name)} of {name}.")
        else:
            print(f"Failed to remove {amount} of {name}.")

    def makeMeal(self):
        self.meal.setName(input("Enter meal name: "))

        while True:
            food_name = input("Enter food name to add to meal (or 'done' to finish): ")
            if food_name.lower() == 'done':
                break
            amount = float(input("Enter amount: "))
            if self.meal.addFood(food_name, amount):
                print(f"Added {amount} of {food_name} to the meal.")
            else:
                print(f"Failed to add {food_name} to the meal.")

        print("Meal created:", self.meal.getMeal())



if __name__ == '__main__':
    Main()