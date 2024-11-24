import unittest
from fundamentals import check_numbers

class TestCheckNumber(unittest.TestCase):
    def testCheckNumber(self):
        self.assertEqual(check_numbers(0), "Neutral")
        self.assertEqual(check_numbers(15), "Weird")
    
    def test_check_number_even_range_2_to_5(self):
        self.assertEqual(check_numbers(2), "Not weird")
            
    def test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_numbers(20), "Weird")
        
    def  test_check_number_even_greater_than_20(self):
        self.assertEqual(check_numbers(21), "Not weird")
        
    def  test_check_number_negative_even_number(self):
        self.assertEqual(check_numbers(-2), "Very weird")
        
    def test_check_number_negative_odd_number(self):
        self.assertEqual(check_numbers(-1), "Extremely weird")
        
    def test_check_number_neutral(self):        
       self.assertEqual(check_numbers(0), "Neutral")

if __name__ == '__main__':
    unittest.main()