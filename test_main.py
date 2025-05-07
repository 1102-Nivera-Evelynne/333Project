import unittest
from main import Main
from unittest.mock import patch
from user import User
#coverage run -m unittest discover
#coverage report -m

class TestMain(unittest.TestCase):

    @patch.object(Main, "begin")
    def setUp(self, mockBegin):
        self.main = Main()
        user = User()
        user.setName("John Doe")
        user2 = User()
        user2.setName("Jane Doe")
        self.main.users.append(user)
        self.main.users.append(user2)
        

    @patch("builtins.input", side_effect=["Apple", "2", "9"])
    @patch("builtins.print")
    def testSendFoodToUser(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.users[0].pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)

        with self.assertRaises(SystemExit):  
            self.main.sendFood(self.main.users[1])

        self.assertEqual(self.main.users[0].pantry.getFoodAmount("Apple"), 3)
        self.assertEqual(self.main.users[1].pantry.getFoodAmount("Apple"), 2)

    @patch("builtins.input", side_effect=["Apple", "52", "14", "0.3", "5", "9"])
    @patch("builtins.print")
    def testInsertFoodToPantry(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.pantry.foods = []

        with self.assertRaises(SystemExit): 
            self.main.insertFood()

        self.assertEqual(len(self.main.currentUser.pantry.foods), 1)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].calories, 52)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].carbs, 14)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].protein, 0.3)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].unit, "")
        self.assertEqual(self.main.currentUser.pantry.foods[0]["amount"], 5)

    @patch("builtins.input", side_effect=["Apple", "2", "9"])
    @patch("builtins.print")
    def testRemoveFoodFromPantry(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)

        with self.assertRaises(SystemExit):  
            self.main.removeFood()
        
        self.assertEqual(self.main.currentUser.pantry.getFoodAmount("Apple"), 3)


    @patch("builtins.input", side_effect=["Breakfast", "2", "Apple", "2", "Banana", "3", "9"])
    @patch("builtins.print")
    def testCreateMeal(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.main.currentUser.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)

        with self.assertRaises(SystemExit):
            self.main.createMeal()

        self.assertEqual(len(self.main.currentUser.meals), 1)
        self.assertEqual(self.main.currentUser.meals[0].name, "Breakfast")
        self.assertEqual(len(self.main.currentUser.meals[0].foods), 2)
        self.assertEqual(self.main.currentUser.meals[0].foods[0]["food"].name, "Apple")
        self.assertEqual(self.main.currentUser.meals[0].foods[0]["amount"], 2)
        self.assertEqual(self.main.currentUser.meals[0].foods[1]["food"].name, "Banana")
        self.assertEqual(self.main.currentUser.meals[0].foods[1]["amount"], 3)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["amount"], 3)
        self.assertEqual(self.main.currentUser.pantry.foods[1]["amount"], 1)

    @patch("builtins.input", side_effect=["Breakfast", "9"])
    @patch("builtins.print")
    def testRemoveMeal(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.createMeal("Breakfast")
        self.main.currentUser.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.main.currentUser.addFoodToMeal("Breakfast", "Apple", 2)

        with self.assertRaises(SystemExit):  
            self.main.removeMeal()

        self.assertEqual(len(self.main.currentUser.meals), 0)
        self.assertEqual(len(self.main.currentUser.pantry.foods), 1)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["amount"], 5)

    @patch("builtins.input", side_effect=["John Doe", "9"])
    @patch("builtins.print")
    def testLogin(self, mockPrint, mockInput):
        self.main.currentUser = None
        
        with self.assertRaises(SystemExit):  
            self.main.login()

        self.assertEqual(self.main.currentUser.getName(), "John Doe")


    @patch("builtins.input", side_effect=["User", "2"])
    @patch("builtins.print")
    def testLoginInvalid(self, mockPrint, mockInput):
        self.main.currentUser = None
        
        with self.assertRaises(SystemExit):  
            self.main.login()

        self.assertEqual(self.main.currentUser, None)

    @patch("builtins.input", side_effect=["John Doe", "9"])
    @patch("builtins.print")    
    def testOnSuccessfulLogin(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        with self.assertRaises(SystemExit):  
            self.main.login()

    @patch("builtins.input", side_effect=["9"])
    @patch("builtins.print")    
    def testDisplayMeals(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.createMeal("Breakfast")
        self.main.currentUser.createMeal("Lunch")
        with self.assertRaises(SystemExit):  
            self.main.displayMeals()

        self.assertEqual(len(self.main.currentUser.meals), 2)
        self.assertEqual(self.main.currentUser.meals[0].name, "Breakfast")
        self.assertEqual(self.main.currentUser.meals[1].name, "Lunch")

    @patch("builtins.input", side_effect=["User", "2", "User", "9"])
    @patch("builtins.print") 
    def testCreateUser(self, mockPrint, mockInput):
        self.main.currentUser = None

        with self.assertRaises(SystemExit):  
            self.main.createUser()

        self.assertEqual(len(self.main.users), 3)
        self.assertEqual(self.main.users[2].getName(), "User")

    @patch("builtins.input", side_effect=["Apple", "2", "9"])
    @patch("builtins.print") 
    def testAddExistingFoodToPantry(self, mockPrint, mockInput):
        self.main.currentUser = self.main.users[0]
        self.main.currentUser.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        
        with self.assertRaises(SystemExit):  
            self.main.insertFood()
        
        self.assertEqual(len(self.main.currentUser.pantry.foods), 1)
        self.assertEqual(self.main.currentUser.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.main.currentUser.pantry.foods[0]["amount"], 7)

    @patch("builtins.input", side_effect=["3"])
    @patch("builtins.print") 
    def testExistFromBegin(self, mockPrint, mockInput):
        self.main.currentUser = None
        with self.assertRaises(SystemExit):  
            self.main.begin()


if __name__ == '__main__':
    unittest.main()
        