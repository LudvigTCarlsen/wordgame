import unittest
import functions

class testCases(unittest.TestCase):
    
    def setUp(self):
        

    def tearDown(self):
        pass

    def test_sum(self):
        lst = [1,2,3,4,5]
        actualvalue = summa.sum(lst)
        self.assertEqual(actualvalue,15)

    def test_times(self):
        lst=[3.5,2]
        actualvalue = summa.times(lst)
        self.assertEqual(actualvalue, 3)

if __name__ == "__main__":
    unittest.main()