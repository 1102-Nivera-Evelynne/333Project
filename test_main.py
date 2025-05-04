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

if __name__ == '__main__':
    unittest.main()
        