import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def gcd(num1, num2):
    pass

# DO NOT TOUCH THE BELOW CODE
class TestGcd(unittest.TestCase):
    
    def test_01(self):
        self.assertEqual(gcd(3, 6), 3)

    def test_02(self):
        self.assertEqual(gcd(1, 5), 1)
    
    def test_03(self):
        self.assertEqual(gcd(10, 20), 10)

    def test_04(self):
        self.assertEqual(gcd(4, 8), 4)    


if __name__ == '__main__':
    unittest.main(verbosity=2)

