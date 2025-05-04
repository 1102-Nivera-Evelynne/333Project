import unittest
from pantry import Pantry

#coverage run -m unittest discover
#coverage report -m

class TestFood(unittest.TestCase):
    def setUp(self):
        self.pantry = Pantry()

    def testCheckFoodInPantryFalse(self):
        self.assertFalse(self.pantry.checkFoodInPantry("Apple"))
    
    def testCheckFoodInPantryTrue(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertTrue(self.pantry.checkFoodInPantry("Apple"))

    def testAddNewFood(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertEqual(len(self.pantry.foods), 1)
        self.assertEqual(self.pantry.foods[0]["food"].name, "Apple")
        self.assertEqual(self.pantry.foods[0]["amount"], 5)

    def testAddExistingFood(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.pantry.addFoodExists("Apple", 3)
        self.assertEqual(self.pantry.foods[0]["amount"], 8)

    def testAddNewFoodInvalidAmount(self):
        with self.assertRaises(TypeError):
            self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", "five")
    
    def testAddNewFoodInvalidValue(self):
        with self.assertRaises(TypeError):
            self.pantry.addFoodNotExist("Apple", "fifty-two", 14, 0.3, "", 5)
    
    def testAddExistingFoodInvalidAmount(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        with self.assertRaises(TypeError):
            self.pantry.addFoodExists("three")

    def testRemoveFoodAllFood(self):
        self.pantry.addFoodNotExist("Apple",52, 14, 0.3, "", 5)
        self.assertTrue(self.pantry.removeFood("Apple", 5))
        self.assertFalse(self.pantry.checkFoodInPantry("Apple"))

    def testRemoveFoodPartial(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertTrue(self.pantry.removeFood("Apple", 3))
        self.assertEqual(self.pantry.getFoodAmount("Apple"), 2)
    
    def testRemoveFoodNotInPantry(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertFalse(self.pantry.removeFood("Banana", 3))
    
    def testRemoveFoodTooMuch(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        self.assertFalse(self.pantry.removeFood("Apple", 6))

    def testGetFood(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        food = self.pantry.getFood("Apple")
        self.assertEqual(food.name, "Apple")
        self.assertEqual(food.calories, 52)
        self.assertEqual(food.carbs, 14)
        self.assertEqual(food.protein, 0.3)
        self.assertEqual(food.unit, "")
    
    def testGetFoodNotInPantry(self):
        self.pantry.addFoodNotExist("Apple", 52, 14, 0.3, "", 5)
        food = self.pantry.getFood("Banana")
        self.assertIsNone(food)

if __name__ == '__main__':
    unittest.main()