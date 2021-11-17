import unittest
from defin import adding

class Activitytests(unittest.TestCase):
    def test_adding(self):
        self.assertEqual(adding(0,5)
        ,"no")
    def test_adding2(self):
        self.assertEqual(adding(11,5)
        ,"hello")   


if __name__=="__main__":
    unittest.main()
