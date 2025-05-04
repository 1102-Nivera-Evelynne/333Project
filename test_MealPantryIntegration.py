import unittest
from pantry import Pantry
from meal import Meal

#coverage run -m unittest discover
#coverage report -m

class TestMealAndPantry(unittest.TestCase):
    def setUp(self):
        self.pantry = Pantry()
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodNotExist("Banana", 89, 23, 1.1, "", 4)

    def testAddFoodToMeal(self):
        meal = Meal()
        meal.setPantry(self.pantry)
        meal.setName("Fruits")
        meal.addFood("Apple", 2)
        meal.addFood("Banana", 3)
        
        self.assertEqual(len(meal.foods), 2)
        self.assertEqual(meal.foods[0]["food"].name, "Apple")
        self.assertEqual(meal.foods[0]["amount"], 2)
        self.assertEqual(meal.foods[1]["food"].name, "Banana")
        self.assertEqual(meal.foods[1]["amount"], 3)

        self.assertEqual(len(self.pantry.foods), 2)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 3)
        self.assertEqual(self.pantry.foods[1]["food"].name, "Banana")
        self.assertEqual(self.pantry.foods[1]["amount"], 1)

    def testAddAllFoodToMeal(self):
        meal = Meal()
        meal.setPantry(self.pantry)
        meal.setName("Fruits")
        meal.addFood("Apple", 5)
        meal.addFood("Banana", 4)
        
        self.assertEqual(len(meal.foods), 2)
        self.assertEqual(meal.foods[0]["food"].name, "Apple")
        self.assertEqual(meal.foods[0]["amount"], 5)
        self.assertEqual(meal.foods[1]["food"].name, "Banana")
        self.assertEqual(meal.foods[1]["amount"], 4)

        self.assertEqual(len(self.pantry.foods), 0)

if __name__ == '__main__':
    unittest.main()