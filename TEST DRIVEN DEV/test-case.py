import unittest

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)
    
    def test_add_zero(self):
        result = add_numbers(10, 0)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
