import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def minimum(num1, num2, num3):
    pass    
   


# DO NOT TOUCH THE BELOW CODE
class TestMinimum(unittest.TestCase):

    def test_01(self):
        self.assertEqual(minimum(3,5,10), 3)

    def test_02(self):
        self.assertEqual(minimum(-3,5,10), -3)

    def test_03(self):
        self.assertEqual(minimum(-3,5,0), -3)


if __name__ == '__main__':
    unittest.main(verbosity=2)

