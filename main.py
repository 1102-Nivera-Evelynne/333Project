from food import Food
from meal import Meal
from user import User

class Main:
    def __init__(self):
        self.meal = Meal()
        self.pantry = self.meal.pantry
        self.food = Food()
        self.users = []

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
                return True
        print(f"User with name {name} does not exist. What would you like to do?")
        print("1. Create User")
        print("2. Exit")
        choice = input()
        if choice == "1":
            self.createUser()
        elif choice == "2":
            print("Goodbye!")
            exit()

    def onSuccessfulLogin(self):
        print("What would you like to do?")
        print("1. Add food to pantry")
        print("2. Remove food from pantry")
        print("3. Create meal")
        print("4. Switch user")
        print("5. Exit")
        choice = input()

        if choice == "1":
           # self.insertFood()
           pass
        elif choice == "2":
           # self.removeFood()
           pass
        elif choice == "3":
           # self.makeMeal()
           pass
        elif choice == "4":
           # print("Goodbye!")
           # exit()
           pass

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