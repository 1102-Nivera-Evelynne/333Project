import unittest
from food import Food
from meal import Meal

#coverage run -m unittest discover
#coverage report -m

class TestMeal(unittest.TestCase):
    def setUp(self):
        self.meal = Meal()
        self.apple = Food()
        #Food attributes: name, calories, carbs, protein, unit
        self.apple.setAttributes("Apple", 52, 14, 0.3, "")
        self.banana = Food()
        self.banana.setAttributes("Banana", 89, 23, 1.1, "")

    def test_setName(self):
        self.assertTrue(self.meal.setName("Fruits"))
        self.assertEqual(self.meal.name, "Fruits")
    
    def test_setName_empty(self):
        self.assertFalse(self.meal.setName(""))
        self.assertEqual(self.meal.name, "")    

    def test_calculateNutritionalValues(self):
        self.meal.foods.append({"food" : self.apple, "amount": 2})
        self.meal.foods.append({"food" : self.banana, "amount": 4})
        self.assertEqual(self.meal.calculateNutritionalValues(), (460, 120, 5.0))

    def test_getMeal(self):
        self.meal.foods.append({"food" : self.apple, "amount": 2})
        self.meal.foods.append({"food" : self.banana, "amount": 4})
        self.meal.setName("Fruits")
        mealName = "Fruits"
        mealFoods = [{"food": "Apple", "amount": 2}, {"food": "Banana", "amount": 4}]
        mealCalories = 460
        mealCarbs = 120
        mealProtein = 5.0
        self.meal.calculateNutritionalValues()
        self.assertEqual(self.meal.getMeal()["name"], mealName)
        self.assertEqual(self.meal.getMeal()["foods"], mealFoods)
        self.assertEqual(self.meal.getMeal()["calories"], mealCalories)
        self.assertEqual(self.meal.getMeal()["carbs"], mealCarbs)
        self.assertEqual(self.meal.getMeal()["protein"], mealProtein)

    def test_resetMeal(self):
        self.meal.foods.append({"food" : self.apple, "amount": 2})
        self.meal.foods.append({"food" : self.banana, "amount": 4})
        self.assertTrue(self.meal.resetMeal())
        self.assertEqual(self.meal.foods, [])
        self.assertEqual(self.meal.calories, 0)
        self.assertEqual(self.meal.carbs, 0)
        self.assertEqual(self.meal.protein, 0)
        self.assertEqual(self.meal.name, "")