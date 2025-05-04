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
        print("1. Add food to pantry")
        print("2. Remove food from pantry")
        print("3. Create meal")
        print("4. Switch user")
        print("5. Exit")
        choice = input()

        if choice == "1":
           self.insertFood()
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
        food = input("Enter food name: ")
        if self.currentUser.checkFoodInPantry(food):
            amount = input("Looks like you already own some of that food. Enter amount you'd like to add: ")
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
                self.onSuccessfulLogin(self.currentUser.getName())
                
            else:
                print(f"Failed to add {food}.")
                self.onSuccessfulLogin(self.currentUser.getName())

if __name__ == '__main__':
    Main()