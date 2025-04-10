import unittest
from food import Food

#coverage run -m unittest discover
#coverage report -m

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()
        self.food.setAttributes("Apple", 52, 14, 0.3, "")

    def testAttributes(self):
        self.assertEqual(self.food.name, "Apple")
        self.assertEqual(self.food.calories, 52)
        self.assertEqual(self.food.carbs, 14)
        self.assertEqual(self.food.protein, 0.3)
        self.assertEqual(self.food.unit, "")

    def testAttributesNonNumeric(self):
        with self.assertRaises(TypeError):
            self.food.setAttributes("Apple", "fifty-two", 14, 0.3, "")

if __name__ == '__main__':
    unittest.main()