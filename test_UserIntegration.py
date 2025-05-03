import unittest
from user import User

#coverage run -m unittest discover
#coverage report -m

class TestUserIntegration(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.setName("John Doe")
        self.pantry = self.user.getPantry()
    
    def testAddFoodToPantry(self):
        self.pantry.foodName = "Apple"
        self.pantry.addFoodNotExist(52, 14, 0.3, "", 5)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 5)
    
    def testAddExistingFoodToPantry(self):
        self.pantry.foodName = "Apple"
        self.pantry.addFoodNotExist(52, 14, 0.3, "", 5)
        self.pantry.addFoodExists(3)
        self.assertEqual(self.pantry.foods[0]["amount"], 8)

    def testRemoveFoodFromPantry(self):
        self.pantry.foodName = "Apple"
        self.pantry.addFoodNotExist(52, 14, 0.3, "", 5)
        self.assertTrue(self.pantry.removeFood("Apple", 3))
        self.assertEqual(self.pantry.getFoodAmount("Apple"), 2)

    def testMealCreation(self):
        self.assertTrue(self.user.createMeal("Breakfast"))
        self.assertEqual(len(self.user.meals), 1)
        self.assertEqual(self.user.meals[0].name, "Breakfast")

    def testAddFoodToMeal(self):
        self.user.createMeal("Breakfast")
        self.assertFalse(self.user.addFoodToMeal("Breakfast", "Apple", 2))

    def testAddFoodToMealValid(self):
        self.user.meals = []
        self.pantry.foodName = "Apple"
        self.pantry.addFoodNotExist(52, 14, 0.3, "", 5)
        self.assertTrue(self.user.createMeal("Breakfast"))
        self.assertTrue(self.user.addFoodToMeal("Breakfast", "Apple", 2))
        meal = self.user.getMeal("Breakfast")
        self.assertEqual(meal.name, "Breakfast")
        self.assertEqual(len(meal.foods), 1)
        self.assertEqual(meal.foods[0]["food"].name, "Apple")
        self.assertEqual(meal.foods[0]["amount"], 2)