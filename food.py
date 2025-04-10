class Food:
    def __init__(self):
        self.name = "Food"
        self.calories = 0
        self.carbs = 0
        self.protein = 0
        self.unit = "grams"

    def setAttributes(self, name, calories, carbs, protein, unit):
        if not all(isinstance(x, (int, float)) for x in [calories, carbs, protein]):
            raise TypeError("Please enter numeric values for calories, carbs, and protein.")
        
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.unit = unit