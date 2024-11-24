import unittest
from fundamentals import check_number
import fundamentals as fund

class TestCheckNumber(unittest):
    def testCheckNumber(self):
        self.assertEqual(fund.check_number(0), "Neutral")
        self.assertEqual(fund.check_number(15), "Weird")
        

if __name__ == '__main__':
    unittest.main()