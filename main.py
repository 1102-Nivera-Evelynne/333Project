from food import Food
from meal import Meal
from user import User

class Main:
    def __init__(self):
        self.meal = Meal()
        self.pantry = self.meal.pantry
        self.food = Food()
        self.users = []
        self.currentUser = None

        self.begin()

    def begin(self):
        print("Welcome to Food Logger! What would you like to do?")
        print("1. Create User")
        print("2. Log in")
        print("3. Exit")
        choice = input()

        if choice == "1":
            self.createUser()
        if choice == "2":
            self.login()

    def createUser(self):
        name = input("Enter your name: ")
        user = User()
        name = str(name)

        for users in self.users:
            if name == users.getName():
                print(f"User with name {name} already exists. Please choose a different name.")
                self.createUser()

        if user.setName(name):
            self.users.append(user)
            print(f"'{name}' has been added. You can now log in with this name.")
            self.begin()
        else:
            print(f"Failed to create user with name {name}. Name cannot be empty.")
            self.createUser()

    def login(self):
        name = input("Enter your name: ")
        for user in self.users:
            if user.getName() == name:
                print(f"Welcome back, {name}!")
                self.onSuccessfulLogin(name)
        print(f"User with name {name} does not exist. What would you like to do?")
        print("1. Create User")
        print("2. Exit")
        choice = input()
        if choice == "1":
            self.createUser()
        elif choice == "2":
            print("Goodbye!")
            exit()

    def onSuccessfulLogin(self, name):
        for user in self.users:
            if user.getName() == name:
                self.currentUser = user
        print("What would you like to do?")
        print("1. Display pantry")
        print("2. Add food to pantry")
        print("3. Remove food from pantry")
        print("4. Create meal")
        print("5. Display meals")
        print("6. Remove meal")
        print("7. Switch user")
        print("8. Exit")
        choice = input()

        if choice == "1":
            self.displayPantry()
        elif choice == "2":
            self.insertFood()
        elif choice == "3":
            self.removeFood()
        elif choice == "4":
            self.createMeal()
        elif choice == "5":
            self.displayMeals()
        elif choice == "6":
            self.removeMeal()
        

    def insertFood(self):
        food = input("Enter food to add: ")
        if self.currentUser.checkFoodInPantry(food):
            amount = input("Looks like you already own some of that food. Enter amount you'd like to add: ")
            amount = float(amount)
            if self.currentUser.addExistingFood(food, amount):
                print(f"{amount} of {food} has been added to the pantry.")
            else:
                print(f"Failed to add {food}.")
        else:
            print(f"Looks like {food} is not in your pantry. Please enter the following information to add it:")
            calories = input("Enter calories: ")
            carbs = input("Enter carbs: ")
            protein = input("Enter protein: ")
            unit = input("Enter unit: ")
            amount = input("Enter amount: ")
            if self.currentUser.addNewFood(food, float(calories), float(carbs), float(protein), unit, float(amount)):
                print(f"{amount} of {food} has been added to the pantry.")
                
            else:
                print(f"Failed to add {food}.")

        self.onSuccessfulLogin(self.currentUser.getName())

    def removeFood(self):
        food = input("Enter food to remove: ")
        if self.currentUser.checkFoodInPantry(food):
            amount = input(f"Enter amount of {food} to remove: ")
            amount = float(amount)
            if self.currentUser.removeFood(food, amount):
                print(f"{amount} of {food} has been removed from the pantry.")
                self.onSuccessfulLogin(self.currentUser.getName())
            else:
                print(f"Failed to remove {food}.")
                self.onSuccessfulLogin(self.currentUser.getName())
        else:
            print(f"{food} is not in your pantry. Please add it to the pantry first")
            self.onSuccessfulLogin(self.currentUser.getName())

    def displayPantry(self):
        print("Your pantry contains:")
        for food in self.currentUser.getPantry().foods:
            print(f"{food['food'].name}: {food['amount']}")
        
        self.onSuccessfulLogin(self.currentUser.getName())

    def displayMeals(self):
        print("Your meals:")
        for meal in self.currentUser.meals:
            print(f"{meal.getName()}: {meal.getMeal()}")
            print(f"    Calories: {meal.calories}, Carbs: {meal.carbs}, Protein: {meal.protein}")

        values = self.currentUser.getNutritionalValues()
        print(f"Total Nutrition: Calories: {values[0]}, Carbs: {values[1]}, Protein: {values[2]}")
        self.onSuccessfulLogin(self.currentUser.getName())

    def createMeal(self):
        mealName = input("Enter meal name: ")
        if self.currentUser.createMeal(mealName):
            print(f"Meal '{mealName}' added.")
            print("How many types of food would you like to add to this meal?")
            foodCount = input()
            foodCount = int(foodCount)
        else:
            print(f"Failed to add meal '{mealName}'.")
            self.onSuccessfulLogin(self.currentUser.getName())

        for i in range(foodCount):
            self.addFoodToMeal(mealName)

        self.onSuccessfulLogin(self.currentUser.getName())

    def addFoodToMeal(self, mealName):
        foodName = input("Enter food name to add to meal: ")
        if self.currentUser.checkFoodInPantry(foodName):
            amount = input(f"Enter amount of {foodName} to add to meal: ")
            amount = float(amount)
            if self.currentUser.addFoodToMeal(mealName, foodName, amount):
                print(f"{amount} of {foodName} has been added to meal '{mealName}'.")
            else:
                print(f"Failed to add {foodName} to meal '{mealName}'.")
        else:
            print(f"{foodName} is not in your pantry. Please add it to the pantry first.")

    def removeMeal(self):
        mealName = input("Enter meal name to remove: ")
        if self.currentUser.removeMeal(mealName):
            print(f"Meal '{mealName}' removed. Food from this meal has been returned to the pantry.")
        else:
            print(f"Failed to remove meal '{mealName}'.")
        
        self.onSuccessfulLogin(self.currentUser.getName())

if __name__ == '__main__':
    Main()