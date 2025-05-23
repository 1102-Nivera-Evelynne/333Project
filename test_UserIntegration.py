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
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 5)
    
    def testAddExistingFoodToPantry(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodExists("Apple", 3)
        self.assertEqual(self.pantry.foods[0]["amount"], 8)

    def testRemoveFoodFromPantry(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
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
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)
        self.assertTrue(self.user.createMeal("Breakfast"))
        self.assertTrue(self.user.addFoodToMeal("Breakfast", "Apple", 2))
        self.assertTrue(self.user.addFoodToMeal("Breakfast", "Banana", 3))
        meal = self.user.getMeal("Breakfast")
        self.assertEqual(meal.name, "Breakfast")
        self.assertEqual(len(meal.foods), 2)
        self.assertEqual(meal.foods[0]["food"].name, "Apple")
        self.assertEqual(meal.foods[1]["food"].name, "Banana")
        self.assertEqual(meal.foods[0]["amount"], 2)
        self.assertEqual(meal.foods[1]["amount"], 3)
        self.assertEqual(self.pantry.foods[0]["amount"], 3)
        self.assertEqual(self.pantry.foods[1]["amount"], 1)

    def testAddFoodToMealInvalid(self):
        self.user.createMeal("Breakfast")
        self.assertEqual((self.user.addFoodToMeal("Lunch", "Banana", 2)), "Meal not found.")

    def testRemoveMeal(self):
        self.user.createMeal("Breakfast")
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.user.addFoodToMeal("Breakfast", "Apple", 2)
        self.assertTrue(self.user.removeMeal("Breakfast"))
        self.assertEqual(len(self.user.meals), 0)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["amount"], 5)

    def testRemoveMealInvalid(self):
        self.user.createMeal("Breakfast")
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.user.addFoodToMeal("Breakfast", "Apple", 2)
        self.assertEqual((self.user.removeMeal("Lunch")), "Meal not found.")
        self.assertEqual(len(self.user.meals), 1)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["amount"], 3)

    def testRemoveMealMixExistingAndNew(self):
        self.user.meals = []
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)
        self.user.createMeal("Breakfast")
        self.user.addFoodToMeal("Breakfast", "Apple", 2)
        self.user.addFoodToMeal("Breakfast", "Banana", 4)
        meal = self.user.getMeal("Breakfast")
        self.assertEqual(meal.name, "Breakfast")
        self.assertEqual(len(meal.foods), 2)
        self.assertEqual(meal.foods[0]["food"].name, "Apple")
        self.assertEqual(meal.foods[1]["food"].name, "Banana")
        self.assertEqual(meal.foods[0]["amount"], 2)
        self.assertEqual(meal.foods[1]["amount"], 4)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 3)
        self.assertFalse(self.pantry.checkFoodInPantry("Banana"))

        self.assertTrue(self.user.removeMeal("Breakfast"))
        self.assertEqual(len(self.user.meals), 0)
        self.assertEqual(len(self.pantry.foods), 2)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 5)
        self.assertEqual(self.pantry.foods[1]["food"].name, "Banana")
        self.assertEqual(self.pantry.foods[1]["amount"], 4)

    def testGetNutritionalValues(self):
        self.user.meals = []
        self.user.createMeal("Breakfast")
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)
        self.user.addFoodToMeal("Breakfast", "Apple", 2)
        self.user.addFoodToMeal("Breakfast", "Banana", 4)
        meal = self.user.getMeal("Breakfast")
        mealInfo = meal.calculateNutritionalValues()
        values = self.user.getNutritionalValues()
        self.assertEqual(mealInfo[0], values[0])
        self.assertEqual(mealInfo[1], values[1])
        self.assertEqual(mealInfo[2], values[2])

    def testGetNutritionalValuesMultipleMeals(self):
        self.user.meals = []
        self.user.createMeal("Breakfast")
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)
        self.user.addFoodToMeal("Breakfast", "Apple", 2)
        self.user.addFoodToMeal("Breakfast", "Banana", 4)
        self.user.createMeal("Lunch")
        self.pantry.addFoodNotExist("Chicken", 239, 0, 27, "g", 3)
        self.pantry.addFoodNotExist("Rice", 130, 28, 2.7, "g", 2)
        self.user.addFoodToMeal("Lunch", "Chicken", 1)
        self.user.addFoodToMeal("Lunch", "Rice", 1)
        values = self.user.getNutritionalValues()
        self.assertEqual(len(self.user.meals), 2)
        self.assertEqual(values[0], 460 + 239 + 130)
        self.assertEqual(values[1], 120 + 28)
        self.assertEqual(values[2], 5.0 + 2.7 + 27)

if __name__ == '__main__':
    unittest.main()